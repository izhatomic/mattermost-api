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

    def update_user_status(self,
                           user_id: str,
                           status: str,
                           dnd_end_time: int) -> dict:
        """
        Manually set a user's status. When setting a user's status, the status will remain that value until set "online" again, which will return the status to being automatically updated based on user activity.

        Must have edit_other_users permission for the team.

        :param user_id: User ID.
        :param status: User status, can be online, away, offline and dnd.
        :param dnd_end_time: Time in epoch seconds at which a dnd status would be unset.
        :return: User status update info.
        """

        url = f"{self.api_url}/{user_id}/status"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('user_id', user_id)
        self.add_to_json('status', status)
        if dnd_end_time is not None:
            self.add_to_json('dnd_end_time', dnd_end_time)

        return self.request(url, request_type='PUT', body=True)
