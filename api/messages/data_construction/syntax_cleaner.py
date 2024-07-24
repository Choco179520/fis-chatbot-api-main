import re
import os

from unidecode import unidecode

from api.messages.data_construction.base_data_builder import BaseDataBuilder


class SyntaxCleaner(BaseDataBuilder):
    """Concrete data builder that removes irrelevant symbols, removes tildes and converts characters to lowercase."""

    def build_data(self, data: list[str]) -> list[str]:
        """
        Process the data set to remove irrelevant symbols, remove tildes and converts characters to lowercase.

        :param data: The data set that will be processed by the current data builder.
        """

        if os.getenv('SYNTAX_CLEANER', 'False') == 'True':
            built_data: list[str] = []

            for data_phrase in data:
                # Remove tildes and converts characters to lowercase
                unidecode_data = unidecode(data_phrase.lower())

                # Remove irrelevant symbols and save the cleaned phrase
                built_data.append(self._remove_symbols(unidecode_data))

            return super().build_data(built_data)

        return super().build_data(data)

    @staticmethod
    def _remove_symbols(data_phrase: str) -> str:
        """
        Remove irrelevant symbols.

        :param data_phrase: The data phrase that will be cleaned.
        :return: The cleaned phrase without irrelevant symbols.
        """

        return re.sub(r'[^a-zA-Z0-9\s]', '', data_phrase)
