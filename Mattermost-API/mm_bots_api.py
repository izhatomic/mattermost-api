from typing import Union, List, Dict
from Mattermost_Base import Base


class Bots(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/bots"

    def convert_user_into_bot(self, user_id: str) -> dict:
        """
        Convert a user into a bot.

        Minimum server version: 5.26

        Must have manage_system permission.

        :param user_id: User GUID
        :return: User conversion info
        """

        url = f"{self.base_url}/users/{user_id}/convert_to_bot"

        self.reset()

        return self.request(url, request_type='POST')

    def create_bot(self,
                   username: str,
                   display_name: str,
                   description: str) -> dict:
        """
        Create a new bot account on the system. Username is required.

        Must have create_bot permission.

        Minimum server version: 5.10

        :param username: Bot's name
        :param display_name: Bot's display name
        :param description: Bot's description
        :return: Bot creation info
        """

        url = f"{self.api_url}"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('username', username)
        if display_name is not None:
            self.add_to_json('display_name', display_name)
        if description is not None:
            self.add_to_json('description', description)

        return self.request(url, request_type='POST', body=True)