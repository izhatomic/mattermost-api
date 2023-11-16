from typing import Union, List, Dict
from Mattermost_Base import Base


class Status(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/users"

    def get_user_status(self, user_id: str) -> dict:
        """
        Get user status by id from the server.

        Must be authenticated.

        :param user_id: User ID.
        :return: User status retrieval info.
        """

        url = f"{self.api_url}/{user_id}/status"

        self.reset()

        return self.request(url, request_type='GET')
