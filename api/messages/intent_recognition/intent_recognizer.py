from abc import ABC, abstractmethod

from api.messages.intent_recognition.data_types.intent_recognizer_response import IntentRecognizerResponse
from api.messages.intent_recognition.data_types.intent_recognizer_input_data import IntentRecognizerInputData


class IntentRecognizer(ABC):
    """Interface that is common to all objects that the intent recognizer factory can produce."""

    @abstractmethod
    def verify_user_intent(self, recognizer_input_data: IntentRecognizerInputData) -> IntentRecognizerResponse:
        """
        Process a user message to determine its intent.

        :param recognizer_input_data: Object with the data needed for the intent recognizer to get the user intent.
        :return: An object representing a user intent.
        """
        pass
