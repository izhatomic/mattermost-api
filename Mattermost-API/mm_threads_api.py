from typing import Union, List, Dict
from Mattermost_Base import Base


class Threads(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/users"

    def get_unread_mention_counts_from_followed_threads(self,
                                                        user_id: str,
                                                        team_id: str) -> dict:
        """
        Get all unread mention counts from followed threads.

        Minimum server version: 5.29
        Must be logged in as the user or have edit_other_users permission.

        :param user_id: The ID of the user. This can also be "me" which will point to the current user.
        :param team_id: The ID of the team in which the thread is.
        :return: Upload creation successful.
        """

        url = f"{self.api_url}/{user_id}/teams/{team_id}/threads/mention_counts"

        self.reset()

        return self.request(url, request_type='GET')
