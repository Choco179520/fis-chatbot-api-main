from api.messages.intent_recognition.intent_recognizer_factory import IntentRecognizerFactory
from api.messages.intent_recognition.intent_recognizer import IntentRecognizer
from api.messages.intent_recognition.cosine_similarity import CosineSimilarity


class CosineSimilarityFactory(IntentRecognizerFactory):
    """Concrete intent recognizer factory that creates a recognizer based on cosine similarity."""

    def create_recognizer(self) -> IntentRecognizer:
        """
        Create a recognizer based on cosine similarity.

        :return: A cosine similarity based intent recognizer.
        """
        return CosineSimilarity()
