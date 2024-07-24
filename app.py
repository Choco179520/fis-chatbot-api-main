import requests
import random
import ssl
import os

import nltk
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, Request, request, send_from_directory, jsonify
from flasgger import Swagger
from flask_cors import CORS

from api.messages.data_construction.data_builder import DataBuilder
from api.messages.data_construction.stop_words_cleaner import StopWordsCleaner
from api.messages.data_construction.syntax_cleaner import SyntaxCleaner
from api.messages.data_construction.lemmatizer import Lemmatizer
from api.actions.actions_responses_generator import ActionsResponsesGenerator
from api.proxy.actions_proxy import ActionsProxy
from api.proxy.proxy_interface import ProxyInterface
from api.proxy.messages_proxy import MessagesProxy
from api.messages.messages_responses_generator import MessagesResponsesGenerator
from api.messages.intent_recognition.transformer_based_similarity_network import TransformerBasedSimilarityNetwork
from api.messages.intent_recognition.transformer_based_similarity_network_factory import \
    TransformerBasedSimilarityNetworkFactory
from api.persistence_requests import data_importer

# Create a Flask application
app = Flask(__name__)
app.config['SWAGGER'] = {
    'favicon': '/static/icons/favicon.ico',
    'title': 'FIS Chatbot API REST',
    'hide_top_bar': True,
    'external_specs': None
}

# Define CORS policies and configure Swagger
config = {"swagger_ui": True, "specs_route": "/api/docs"}
swagger = Swagger(app, template_file="swagger.yaml", config=config, merge=True)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Enable the use of reverse proxies
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

# Configure the static route
app.static_folder = 'static'

# Modify SSL certificate to prevent libraries download issues
try:
    # noinspection PyProtectedMember
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download the set of stop words used to filter the data
if os.getenv('STOP_WORDS_CLEANER', 'False') == 'True':
    nltk.download('stopwords')

# Initialize model to reduce load times
intent_recognizer: TransformerBasedSimilarityNetwork = TransformerBasedSimilarityNetworkFactory().create_recognizer()

# Create data construction objects to build data
syntax_cleaner: DataBuilder = SyntaxCleaner()
stop_words_cleaner: DataBuilder = StopWordsCleaner()
lemmatizer: DataBuilder = Lemmatizer()

# Bring the utterances to reduce the time of database queries
data_importer.documents = requests.get(f"{os.getenv('DB_URL')}/documents").json()

# Get the embedding representation of the utterances to reduce processing time
for document in data_importer.documents:
    # Get the utterances of the current document
    document_utterances = syntax_cleaner.build_data(document['utterances'])

    # Limit the number of utterances analyzed
    if int(os.getenv('UTTERANCES_LIMIT')):
        document_corpus = random.sample(
            document_utterances,
            min(int(os.getenv('UTTERANCES_LIMIT')), len(document_utterances))
        )
    else:
        document_corpus = document_utterances

    document['embeddings'] = intent_recognizer.get_embeddings(document_corpus)


@app.route('/api/status')
def status():
    """Gives a response when the server is active."""
    return jsonify({'status': 'up'})


@app.route('/images/<image_name>')
def show_image(image_name):
    """Looks for an image in the static folder."""
    return send_from_directory('static/images', image_name)


@app.route('/api/actions', methods=['POST'])
def get_action_response():
    """Looks for a response based on an action."""
    responses_generator: ActionsResponsesGenerator = ActionsResponsesGenerator()
    actions_proxy: ProxyInterface = ActionsProxy(responses_generator)
    user_request: Request = request

    return actions_proxy.handle_request(user_request)


@app.route('/api/messages', methods=['POST'])
def get_message_response():
    """Looks for a response based on the user's intent and provides an associated response."""
    responses_generator: MessagesResponsesGenerator = MessagesResponsesGenerator()
    messages_proxy: ProxyInterface = MessagesProxy(responses_generator)
    user_request: Request = request

    return messages_proxy.handle_request(user_request)


if __name__ == '__main__':
    # Run the flask app
    app.run(os.getenv('HOST'), int(os.getenv('PORT')))
