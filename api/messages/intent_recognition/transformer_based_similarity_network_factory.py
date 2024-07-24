from api.messages.intent_recognition.intent_recognizer_factory import IntentRecognizerFactory
from api.messages.intent_recognition.transformer_based_similarity_network import TransformerBasedSimilarityNetwork


class TransformerBasedSimilarityNetworkFactory(IntentRecognizerFactory):
    """Concrete intent recognizer factory that creates a recognizer based on a similarity neural network."""

    def create_recognizer(self) -> TransformerBasedSimilarityNetwork:
        """
        Create a recognizer based on a similarity neural network.

        :return: A transformer similarity neural network based intent recognizer.
        """
        return TransformerBasedSimilarityNetwork()
