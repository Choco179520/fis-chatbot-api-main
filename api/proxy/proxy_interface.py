from abc import ABC, abstractmethod

from flask import Request, Response


class ProxyInterface(ABC):
    """Proxy interface used as an intermediary between users and chatbot services."""

    @abstractmethod
    def handle_request(self, user_request: Request) -> Response:
        """
        Manage a request submitted by a user.

        :param user_request: A request submitted by a user.
        :return: A response object generated by a chatbot service.
        """
        pass
