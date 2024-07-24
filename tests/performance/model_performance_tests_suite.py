import unittest
import random
import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer, util

from api.messages.data_construction.stop_words_cleaner import StopWordsCleaner
from api.messages.data_construction.data_builder import DataBuilder
from api.messages.data_construction.lemmatizer import Lemmatizer
from api.messages.data_construction.syntax_cleaner import SyntaxCleaner


class ModelPerformanceTestsSuite(unittest.TestCase):

    def setUp(self):
        # Load environment variables
        load_dotenv()

        # Set current working directories
        current_path = os.path.dirname(os.path.abspath(__file__))
        root_path = os.path.dirname(os.path.dirname(current_path))
        self.fined_tuned_model_path = f"{root_path}/models/{os.getenv('FINED_TUNED_MODEL')}"

        # Create an intent recognizer factory
        self._base_model = SentenceTransformer(os.getenv('BASE_MODEL'))

        # Create data construction objects to build data
        self._syntax_cleaner: DataBuilder = SyntaxCleaner()
        self._stop_words_cleaner: DataBuilder = StopWordsCleaner()
        self._lemmatizer: DataBuilder = Lemmatizer()

        self._syntax_cleaner.set_next_builder(self._stop_words_cleaner)
        self._stop_words_cleaner.set_next_builder(self._lemmatizer)

        # Confidence limits used by a similarity based intent recognizer
        self._confidence_limit: float = float(os.getenv('CONFIDENCE_LIMIT'))
        self._suggestion_limit: float = float(os.getenv('SUGGESTION_LIMIT'))

        # Sample value for the test
        self._sample_value = 3

    def test_given_base_model_is_fine_tuned_then_performance_improves(self):
        # Get documents from a database
        from static.documents import documents
        documents: list[dict] = documents.documents

        # Select a random number of documents and utterances for the test
        documents_corpus = random.sample(documents, len(documents) // self._sample_value)
        user_messages = []

        for document in documents_corpus:
            utterance = random.choice(document['utterances'])
            user_messages.append(utterance)
            document['utterances'].remove(utterance)

        # Build a performance result matrix
        performance_matrix = [['-'] * 3 for _ in range(len(documents) // self._sample_value)]

        # Compute performance with the base model
        for index, user_message in enumerate(user_messages):
            # Save results in performance matrix
            performance_matrix[index][0] = user_message
            performance_matrix[index][1] = self._compute_sentence_similarity(user_message, documents_corpus[index])

        # Compute performance with the fined tuned model
        if os.path.exists(self.fined_tuned_model_path):
            self._base_model = SentenceTransformer(self.fined_tuned_model_path)
        else:
            self._base_model = SentenceTransformer(
                os.getenv('FINED_TUNED_MODEL'),
                use_auth_token=os.getenv('MODEL_TOKEN')
            )

        for index, user_message in enumerate(user_messages):
            # Save results in performance matrix
            performance_matrix[index][2] = self._compute_sentence_similarity(user_message, documents_corpus[index])

        # Get average performance for each model
        base_model_total = 0
        fined_tuned_total = 0

        for model in performance_matrix:
            base_model_total = base_model_total + float(model[1])
            fined_tuned_total = fined_tuned_total + float(model[2])

        base_model_performance = base_model_total / (len(documents) // self._sample_value)
        fined_tuned_model_performance = fined_tuned_total / (len(documents) // self._sample_value)
        performance_improvement = (fined_tuned_model_performance - base_model_performance) * 100

        print(f"\nPERFORMANCE IMPROVEMENT TEST:")
        print(f"Base model performance: {round(base_model_performance, 5)}")
        print(f"Fined tuned model performance: {round(fined_tuned_model_performance, 5)}")
        print(f"Performance improvement: {round(performance_improvement, 2)}%")

        self.assertGreater(fined_tuned_model_performance, base_model_performance)
        self.assertGreater(performance_improvement, 0)

    def test_given_base_model_is_fined_tuned_then_errors_are_reduced(self):
        # Get documents from a database
        from static.documents import documents
        documents: list[dict] = documents.documents

        # Select a random number of documents and utterances for the test
        documents_corpus = random.sample(documents, 2)
        user_message = random.sample(documents_corpus[0]['utterances'], 1)[0]

        # Build a performance result matrix
        performance_matrix = [['-'] * 3 for _ in range(2)]

        for index, document in enumerate(documents_corpus):
            # Save results in performance matrix
            performance_matrix[index][0] = document['id']
            performance_matrix[index][1] = self._compute_sentence_similarity(user_message, document)

        # Compute performance with the fined tuned model
        if os.path.exists(self.fined_tuned_model_path):
            self._base_model = SentenceTransformer(self.fined_tuned_model_path)
        else:
            self._base_model = SentenceTransformer(
                os.getenv('FINED_TUNED_MODEL'),
                use_auth_token=os.getenv('MODEL_TOKEN')
            )

        for index, document in enumerate(documents_corpus):
            # Save results in performance matrix
            performance_matrix[index][2] = self._compute_sentence_similarity(user_message, document)

        based_model_wrong_similarity = max(float(performance_matrix[1][1]), 0)
        fined_tuned_model_wrong_similarity = max(float(performance_matrix[1][2]), 0)
        error_reduction_percentage = (based_model_wrong_similarity - fined_tuned_model_wrong_similarity) * 100

        print(f"\nERROR REDUCTION TEST:")
        print(f"Base model wrong similarity: {round(based_model_wrong_similarity, 5)}")
        print(f"Fined tuned model wrong similarity: {round(fined_tuned_model_wrong_similarity, 5)}")
        print(f"Error reduction: {round(error_reduction_percentage, 2)}%")

        self.assertLess(fined_tuned_model_wrong_similarity, based_model_wrong_similarity)

    def _compute_sentence_similarity(self, user_message, documents_corpus):
        # Build the data used by the model
        user_message = self._syntax_cleaner.build_data([user_message]).pop()
        document_corpus = self._syntax_cleaner.build_data(documents_corpus['utterances'])

        # Get the embeddings representations of the corpus and user message
        corpus_embeddings = self._base_model.encode(document_corpus, convert_to_tensor=True)
        user_message_embeddings = self._base_model.encode([user_message], convert_to_tensor=True)

        # Compute cosine similarities
        cosine_similarities = util.cos_sim(corpus_embeddings, user_message_embeddings)

        # Get the max similarity value of the cosine similarities
        return max(cosine_similarities).item()


if __name__ == '__main__':
    unittest.main()
