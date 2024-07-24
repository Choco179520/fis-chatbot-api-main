import requests
import random
import os

from locust import HttpUser, task, between
from dotenv import load_dotenv

from api.persistence_requests import data_importer


class MyUser(HttpUser):
    """Locust user class to test the performance of the API REST."""

    # Load environment variables
    load_dotenv()

    # Bring the utterances to reduce the time of database queries
    data_importer.documents = requests.get(f"{os.getenv('DB_URL')}/documents").json()

    # Get documents from database
    _documents: list[dict] = data_importer.documents

    wait_time = between(1, 2)

    @task
    def test_api_status(self):
        self.client.get("/api/status")

    @task
    def test_api_messages(self):
        # Select random document and message
        selected_document = random.choice(self._documents)
        selected_message = random.choice(selected_document['utterances'])

        payload = {"user_message": selected_message}
        self.client.post("/api/messages", json=payload)

    @task
    def test_api_actions(self):
        # Select random document
        selected_document = random.choice(self._documents)

        payload = {"action": selected_document['id']}
        self.client.post("/api/actions", json=payload)

    @task
    def test_api_images(self):
        self.client.get("/images/fis_epn_sketch.png")
