from typing import Union, List, Dict
from Mattermost_Base import Base


class Exports(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/exports"

    def list_export_files(self) -> dict:
        """
        Lists all available export files.

        Minimum server version: 5.33
        Must have manage_system permissions.

        :return: List of all available export files
        """

        url = f"{self.api_url}/"

        self.reset()

        return self.request(url, request_type='GET')


