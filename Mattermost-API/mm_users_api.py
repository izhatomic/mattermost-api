from typing import Union, List, Dict
from Mattermost_Base import Base


class Uploads(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/users"

    def login_to_mattermost_server(self,
                                   id: str = None,
                                   login_id: str = None,
                                   token: str = None,
                                   device_id: str = None,
                                   ldap_only: str = None,
                                   password: str = None) -> dict:
        """
        Logins to Mattermost server.

        No permission required

        :param id: User ID for authentication.
        :param login_id: User login_id for authentication.
        :param token: User token for authentication.
        :param device_id: User device_id for authentication.
        :param ldap_only: User ldap_only for authentication.
        :param password: User password for authentication.
        :return: User login info.
        """

        url = f"{self.api_url}/login"

        self.reset()
        self.add_application_json_header()
        if id is not None:
            self.add_to_json('id', id)
        if login_id is not None:
            self.add_to_json('login_id', login_id)
        if token is not None:
            self.add_to_json('token', token)
        if device_id is not None:
            self.add_to_json('device_id', device_id)
        if ldap_only is not None:
            self.add_to_json('ldap_only', ldap_only)
        if password is not None:
            self.add_to_json('password', password)

        return self.request(url, request_type='POST', body=True)
