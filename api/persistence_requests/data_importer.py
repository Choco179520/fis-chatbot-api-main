import os

import requests

documents = None


def get_response_set_by_id(response_id):
    return requests.get(f"{os.getenv('DB_URL')}/response-sets/{response_id}").json()
