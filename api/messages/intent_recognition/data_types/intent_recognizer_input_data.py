from abc import ABC


class IntentRecognizerInputData(ABC):
    """Base class for intent data object needed by an intent recognizer."""

    def __init__(self, user_message: str):
        """
        Constructor.

        :param user_message: A message sent by a user.
        """
        self.user_message = user_message
