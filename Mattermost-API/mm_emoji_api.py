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

    def get_list_of_custom_emoji(self,
                                 page: int,
                                 per_page: int,
                                 sort: str) -> dict:
        """
        Get a page of metadata for custom emoji on the system.
        Since server version 4.7, sort using the sort query parameter.

        Must be authenticated.

        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of emojis per page.
        :param sort: Default: "". Either blank for no sorting or "name" to sort by emoji names.
        Minimum server version for sorting is 4.7.
        :return: Emoji list retrieval info.
        """

        url = f"{self.api_url}/"

        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)
        if sort is not None:
            self.add_to_json('sort', sort)

        return self.request(url, request_type='GET', body=True)

    def get_custom_emoji(self, emoji_id: str) -> dict:
        """
        Get some metadata for a custom emoji.

        Must be authenticated.

        :param emoji_id: Emoji GUID.
        :return: Emoji retrieval info.
        """

        url = f"{self.api_url}/{emoji_id}"

        self.reset()

        return self.request(url, request_type='GET')
