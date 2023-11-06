from typing import Union, List, Dict
from Mattermost_Base import Base


class Roles(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/roles"

    def Get_a_lst_roles(self) -> dict:
        """
        Get a list of all the roles.

        Minimum server version: 5.33
        manage_system permission is required.

        :return: Roles list.
        """
        url = f"{self.api_url}/"
        self.reset()

        return self.request(url, request_type='GET')
