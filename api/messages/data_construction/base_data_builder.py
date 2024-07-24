from dotenv import load_dotenv

from api.messages.data_construction.data_builder import DataBuilder


class BaseDataBuilder(DataBuilder):
    """Base class that contains the common structure for all data builder classes."""

    def __init__(self):
        # Load environment variables
        load_dotenv()

        self._next_builder: DataBuilder | None = None

    def set_next_builder(self, data_builder: DataBuilder):
        """
        Set the following builder data that will be in charge of building the data.

        :param data_builder: The concrete data builder that will build the data.
        """
        self._next_builder = data_builder

    def build_data(self, data: list[str]) -> list[str]:
        """
        Process the data set.

        :param data: The data set that will be processed by the current data builder.
        """

        if self._next_builder is not None:
            return self._next_builder.build_data(data)

        return data
