from typing import Union, List, Dict
from Mattermost_Base import Base


class Bots(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/users"

    def convert_user_into_bot(self,
                              user_id: str) -> dict:
        """
        Convert a user into a bot.

        Minimum server version: 5.26

        Must have manage_system permission.

        :param user_id: User GUID
        :return: User conversion info
        """

        url = f"{self.api_url}/{user_id}/convert_to_bot"

        self.reset()

        return self.request(url, request_type='POST')
