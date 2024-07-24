from torch import Tensor

from api.messages.intent_recognition.data_types.intent_recognizer_input_data import IntentRecognizerInputData


class SimilarityBasedInputData(IntentRecognizerInputData):
    """Concrete class that defines the structure of an object data needed by a similarity based intent recognizer."""

    def __init__(self, user_message: str, confidence_limit: float, message_embeddings: Tensor, document_embeddings: Tensor):
        """
        Constructor.

        :param user_message: A message sent by a user.
        :param confidence_limit: A number that represents the limit of a recognized intent.
        :param message_embeddings: A message represented as embeddings to be used to calculate similarity.
        :param document_embeddings: Group of phrases represented as embeddings to be used to calculate similarity.
        """

        super().__init__(user_message)
        self.confidence_limit: float = confidence_limit
        self.message_embeddings: Tensor = message_embeddings
        self.document_embeddings: Tensor = document_embeddings
