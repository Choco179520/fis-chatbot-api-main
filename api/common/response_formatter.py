from flask import Response, jsonify

from api.persistence_requests import data_importer


class ResponseFormatter:
    """Creates an object that will be sent as a response to a user."""

    @staticmethod
    def get_recognized_response(document: dict) -> Response:
        """
        Create a response object from the information in a document.

        :param document: The document related with the response.
        :return: A response object that will be sent to a user.
        """

        found_document = document.get('response_set_id')

        if document['id'] == 'sugerencias':
            return jsonify({'responses': document['responses']})

        if found_document is None:
            return jsonify({'error': f'¡Vaya! No he podido encontrar el documento con el ID {document["id"]}.'})

        return data_importer.get_response_set_by_id(found_document)

    @staticmethod
    def get_no_recognized_response() -> Response:
        """
        Creates a response object for a message that has not been acknowledged.

        :return: A response object that will be sent to a user.
        """

        unknown_intention = [
            {
                "type": "text",
                "content": "¡Oops! Parece que no tengo una respuesta para ese mensaje. Pero aún puedes acceder a "
                           "la Guía del Estudiante para buscar la información que necesitas:"
            },
            {
                "type": "link",
                "path": "https://atenea.epn.edu.ec/handle/25000/727",
                "name": "Guía del Estudiante"
            },
        ]

        return jsonify({'responses': unknown_intention})
