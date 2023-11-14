from typing import Union, List, Dict
from Mattermost_Base import Base


class saml(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/saml"


    def migrate_user_acc_auth_type_to_saml(self, from:str, matches: dict, auto: bool) -> dict:
        """
        Migrates accounts from one authentication provider to another.
        For example, you can upgrade your authentication provider from email to SAML.
        Minimum server version: 5.28
        Must have manage_system permission.
        :param from: The current authentication type for the matched users.
        :param matches: Users map.
        :param auto: Toggle auto migration.
        :return: User account migration info.
        """
        url = f"{self.base_url}/users/migrate_auth/saml"
        self.reset()
        self.add_application_json_header()
        if from is not None:
            self.add_to_json('from', from)
        if matches is not None:
            self.add_to_json('matches', matches)
        if auto is not None:
            self.add_to_json('auto', auto)

        return self.request(url, request_type='POST', body=True)
