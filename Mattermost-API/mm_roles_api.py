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

    def patch_a_role(self, role_id: str, permissions: list[str]) -> dict:
        """
        Partially update a role by providing only the fields you want to update.
        Omitted fields will not be updated.
        The fields that can be updated are defined in the request body,
        all other provided fields will be ignored.

        Minimum server version: 4.9
        manage_system permission is required.

        :param role_id: Role GUID.
        :param permissions: The permissions the role should grant.
        :return: Role patch info.
        """
        url = f"{self.api_url}/name/{role_id}/patch"
        self.reset()
        self.add_application_json_header()
        if permissions is not None:
            self.add_to_json('permissions', permissions)

        return self.request(url, request_type='PUT', body=True)

    def get_a_list_of_roles_by_name(self, roles_list: list[str]) -> dict:
        """
        Get a list of roles from their names.

        Minimum server version: 4.9
        Requires an active session but no other permissions.

        :param roles_list: List of role names.
        :return: Role list info.
        """
        url = f"{self.api_url}/names"
        self.reset()
        self.add_application_json_header()
        if roles_list is not None:
            self.add_to_json('roles_list', roles_list)

        return self.request(url, request_type='POST', body=True)
