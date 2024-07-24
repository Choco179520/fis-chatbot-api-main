from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from api.messages.intent_recognition.intent_recognizer import IntentRecognizer
from api.messages.intent_recognition.data_types.similarity_based_input_data import SimilarityBasedInputData
from api.messages.intent_recognition.data_types.similarity_based_response import SimilarityBasedResponse


class CosineSimilarity(IntentRecognizer):
    """Concrete intent recognizer that uses a cosine similarity process to recognize the user intent."""

    def verify_user_intent(self, recognizer_input_data: SimilarityBasedInputData) -> SimilarityBasedResponse:
        """
        Determine the user intent based on the user's message and the existing set of phrases.

        :param recognizer_input_data: Object with the data needed for the intent recognizer to get the user intent.
        :return: An object that represents the result of the recognition process.
        """

        # Create the TF-IDF vectorizer
        vectorizer = TfidfVectorizer()

        # Build the TF-IDF array
        tfidf_matrix = vectorizer.fit_transform(
            [recognizer_input_data.user_message] + recognizer_input_data.document_corpus
        )

        # Calculate cosine similarity between sentences
        similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

        # Get the max similarity value of the cosine similarities
        max_similarity_value = max(similarity_matrix[0][1:])

        return SimilarityBasedResponse(
            True if max_similarity_value >= recognizer_input_data.confidence_limit else False,
            max_similarity_value
        )
