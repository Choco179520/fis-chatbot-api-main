from api.messages.intent_recognition.data_types.intent_recognizer_response import IntentRecognizerResponse


class SimilarityBasedResponse(IntentRecognizerResponse):
    """Concrete class that defines the structure of a response of a similarity based intent recognizer."""

    def __init__(self, recognition_status: bool, max_similarity_value: float):
        """
        Constructor.

        :param recognition_status: A boolean value that describes if the intent was recognized.
        :param max_similarity_value: The maximum similarity value found by the intent recognizer.
        """

        super().__init__(recognition_status)
        self.max_similarity_value: float = max_similarity_value
