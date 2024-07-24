from abc import abstractmethod

from api.messages.intent_recognition.intent_recognizer import IntentRecognizer
from api.messages.intent_recognition.data_types.intent_recognizer_input_data import IntentRecognizerInputData
from api.messages.intent_recognition.data_types.intent_recognizer_response import IntentRecognizerResponse


class IntentRecognizerFactory:

    def process_user_intent(self, recognizer_input_data: IntentRecognizerInputData) -> IntentRecognizerResponse:
        """
        Create a generic intent recognizer and process a user intent.

        :param recognizer_input_data: Object with the data needed for the intent recognizer to get a user intent.
        :return: An object representing the result of a user intent.
        """

        intent_recognizer: IntentRecognizer = self.create_recognizer()
        return intent_recognizer.verify_user_intent(recognizer_input_data)

    @abstractmethod
    def create_recognizer(self) -> IntentRecognizer:
        """
        Create a recognizer based on a specific process.

        :return: An intent recognizer based on a specific process.
        """
        pass
