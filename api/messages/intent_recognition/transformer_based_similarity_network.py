import os

from sentence_transformers import SentenceTransformer, util
from huggingface_hub.utils import RepositoryNotFoundError
from dotenv import load_dotenv
from torch import Tensor

from api.messages.intent_recognition.intent_recognizer import IntentRecognizer
from api.messages.intent_recognition.data_types.similarity_based_input_data import SimilarityBasedInputData
from api.messages.intent_recognition.data_types.similarity_based_response import SimilarityBasedResponse


class TransformerBasedSimilarityNetwork(IntentRecognizer):
    """Concrete intent recognizer that uses a transformer based similarity network to get the similarity between
    the corpus and the user message to recognize the user intent."""

    # Load environment variables
    load_dotenv()

    # Singleton object
    _instance: "TransformerBasedSimilarityNetwork" = None

    # Multilingual transformer model based on a similarity network
    _model: SentenceTransformer | None = None

    def __new__(cls):
        """
        Singleton used to reduce the load time of the model.
        """

        if cls._model is None:
            current_path = os.path.dirname(os.path.abspath(__file__))
            root_path = os.path.dirname(os.path.dirname(os.path.dirname(current_path)))
            fined_tuned_model_path = f"{root_path}/models/{os.getenv('FINED_TUNED_MODEL')}"

            try:
                if os.path.exists(fined_tuned_model_path):
                    cls._model = SentenceTransformer(fined_tuned_model_path)
                    print(f"Model downloaded from {fined_tuned_model_path}")
                else:
                    cls._model = SentenceTransformer(
                        os.getenv('FINED_TUNED_MODEL'),
                        use_auth_token=os.getenv('MODEL_TOKEN')
                    )
                    print(f"Model downloaded from {os.getenv('FINED_TUNED_MODEL')}")
            except RepositoryNotFoundError:
                cls._model = SentenceTransformer(os.getenv('BASE_MODEL'))
                print(f"Model downloaded from {os.getenv('BASE_MODEL')}")

            cls._instance = super().__new__(cls)

        return cls._instance

    def verify_user_intent(self, recognizer_input_data: SimilarityBasedInputData) -> SimilarityBasedResponse:
        """
        Determine the user intent based on the similarity of the user message and the current corpus.

        :param recognizer_input_data: Object with the data needed for the intent recognizer to get the user intent.
        :return: An object that represents the result of the recognition process.
        """

        # Compute cosine similarities
        cosine_similarities = util.cos_sim(
            recognizer_input_data.document_embeddings,
            recognizer_input_data.message_embeddings
        )

        # Get the max similarity value of the cosine similarities
        max_similarity_value = max(cosine_similarities).item()

        return SimilarityBasedResponse(
            True if max_similarity_value >= recognizer_input_data.confidence_limit else False,
            max_similarity_value
        )

    def get_embeddings(self, sentences: list[str]) -> Tensor:
        """
        Determines the vector representation of a set of sentences.

        :param sentences: A list of sentences that will be transforms in a vectorial representation.
        :return: A stacked tensor that represents the sentences.
        """
        return self._model.encode(sentences, convert_to_tensor=True)
