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

    def get_user_statuses_by_id(self,
                                user_ids:
                                list[str]) -> dict:
        """
        Get a list of user statuses by id from the server.

        Must be authenticated.

        :param user_ids: User ID.
        :return: User status retrieval info.
        """
        url = f"{self.api_url}/status/ids"

        self.reset()
        self.add_application_json_header()
        if user_ids is not None:
            self.add_to_json('user_ids', user_ids)

        return self.request(url, request_type='POST', body=True)

    def update_user_custom_status(self,
                                  user_id: str,
                                  emoji: str,
                                  text: str,
                                  duration: str,
                                  expires_at: str) -> dict:
        """
        Updates a user's custom status by setting the value in the user's props and updates the user.
        Also save the given custom status to the recent custom statuses in the user's props

        Must be logged in as the user whose custom status is being update.

        :param user_id: User ID.
        :param emoji: Any emoji
        :param text: Any custom status text
        :param duration: Duration of custom status, can be thirty_minutes, one_hour,
        four_hours, today, this_week or date_and_time
        :param expires_at: The time at which custom status should be expired. It should be in ISO format.
        :return: User custom status update info.
        """
        url = f"{self.api_url}/{user_id}/status/custom"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('user_id', user_id)
        self.add_to_json('emoji', emoji)
        self.add_to_json('text', text)
        if duration is not None:
            self.add_to_json('duration', duration)
        if expires_at is not None:
            self.add_to_json('expires_at', expires_at)

        return self.request(url, request_type='PUT', body=True)
