import os

import spacy

from api.messages.data_construction.base_data_builder import BaseDataBuilder


class Lemmatizer(BaseDataBuilder):
    """Concrete data builder that lemmatize words from a list of phrases."""

    def build_data(self, data: list[str]) -> list[str]:
        """
        Process the data set to lemmatize words.

        :param data: The data set that will be processed by the current data builder.
        """

        if os.getenv('LEMMATIZER', 'False') == 'True':
            built_data: list[str] = []

            # Initialize the lemmatizer
            nlp = spacy.load('es_core_news_sm')

            for data_phrase in data:
                built_data.append(" ".join([token.lemma_ for token in nlp(data_phrase)]))

            return super().build_data(built_data)

        return super().build_data(data)
