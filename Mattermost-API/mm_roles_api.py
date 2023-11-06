from typing import Union, List, Dict
from Mattermost_Base import Base


class Roles(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/roles"

    def get_a_lst_roles(self) -> dict:
        """
        Get a list of all the roles.

        Minimum server version: 5.33
        manage_system permission is required.

        :return: Roles list.
        """
        url = f"{self.api_url}/"
        self.reset()

        return self.request(url, request_type='GET')

    def get_a_role(self, role_id: str) -> dict:
        """
        Get a role from the provided role id.

        Minimum server version: 4.9
        Requires an active session but no other permissions.

        :param role_id: Role GUID.
        :return: Role retrieval info.
        """
        url = f"{self.api_url}/{role_id}"
        self.reset()

        return self.request(url, request_type='GET')

    def get_a_role_from_name(self, role_name: str) -> dict:
        """
        Get a role from the provided role name.

        Minimum server version: 4.9
        Requires an active session but no other permissions.

        :param role_name: Role name.
        :return: Role retrieval info.
        """
        url = f"{self.api_url}/name/{role_name}"
        self.reset()

        return self.request(url, request_type='GET')
