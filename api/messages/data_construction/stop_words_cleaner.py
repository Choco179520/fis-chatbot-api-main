import os

from nltk.corpus import stopwords
from unidecode import unidecode

from api.messages.data_construction.base_data_builder import BaseDataBuilder


class StopWordsCleaner(BaseDataBuilder):
    """Concrete data builder that removes stop words from a list of data phrases."""

    def build_data(self, data: list[str]) -> list[str]:
        """
        Process the data set to remove stop word from each spanish phrase of a list.

        :param data: The data set that will be processed by the current data builder.
        """

        if os.getenv('STOP_WORDS_CLEANER', 'False') == 'True':
            built_data: list[str] = []

            # Define stopwords in Spanish
            stopwords_es = set(stopwords.words('spanish'))
            stopwords_es_cleaned = set(unidecode(word) for word in stopwords_es)

            for data_phrase in data:
                built_data.append(' '.join(word for word in data_phrase.split() if word not in stopwords_es_cleaned))

            return super().build_data(built_data)

        return super().build_data(data)
