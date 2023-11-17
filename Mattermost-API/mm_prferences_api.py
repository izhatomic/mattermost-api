from typing import Union, List, Dict
from Mattermost_Base import Base


class Preferences(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/users"

    def get_user_preferences(self, user_id: str) -> dict:
        """
        Get a list of the user's preferences.

        Must be logged in as the user being updated or have the edit_other_users permission.

        :param user_id: User ID.
        :return: User preferences retrieval info.
        """
        url = f"{self.api_url}/{user_id}/preferences"

        self.reset()

        return self.request(url, request_type='GET')

    def save_user_preferences(self,
                              user_id: str,
                              category: str,
                              name: str,
                              value: str) -> dict:
        """
        Save a list of the user's preferences.

        Must be logged in as the user being updated or have the edit_other_users permission.

        :param user_id: User ID.
        :param category: Category.
        :param name: Name.
        :param value: Value.
        :return: User preferences saving info.
        """
        url = f"{self.api_url}/{user_id}/preferences"

        self.reset()
        self.add_application_json_header()
        if user_id is not None:
            self.add_to_json('user_id', user_id)
        if category is not None:
            self.add_to_json('category', category)
        if name is not None:
            self.add_to_json('name', name)
        if value is not None:
            self.add_to_json('value', value)

        return self.request(url, request_type='PUT')
