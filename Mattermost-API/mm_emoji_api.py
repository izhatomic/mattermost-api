from typing import Union, List, Dict
from Mattermost_Base import Base


class Emoji(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/emoji"

    def create_custom_emoji(self,
                            image: str,
                            emoji: str) -> dict:
        """
        Create a custom emoji for the team.

        Must be authenticated.

        :param image: A file to be uploaded.
        :param emoji: A JSON object containing a name field with the name of
        the emoji and a creator_id field with the id of the authenticated user.
        :return: Emoji creation info.
        """

        url = f"{self.api_url}/"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('image', image)
        self.add_to_json('emoji', emoji)

        return self.request(url, request_type='POST', body=True)
