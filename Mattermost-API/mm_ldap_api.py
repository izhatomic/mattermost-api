from typing import Union, List, Dict
from Mattermost_Base import Base


class ldap(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/ldap"

    def migrate_user_acc_auth_type_to_ldap(self, from:str, match_field: str, force: bool) -> dict:
        """
        Migrates accounts from one authentication provider to another. For example, you can upgrade your authentication provider from email to LDAP.

        Minimum server version: 5.28
        Must have manage_system permission.

        :param from: The current authentication type for the matched users.
        :param match_field: Foreign user field name to match.
        :param force: Toggle force migration.
        :return: User account migration info.
        """
        url = f"{self.base_url}/users/migrate_auth/ldap"

        self.reset()
        self.add_application_json_header()
        if from is not None:
            self.add_to_json('from', from)
        if match_field is not None:
            self.add_to_json('match_field', match_field)
        if force is not None:
            self.add_to_json('force', force)

        return self.request(url, request_type='POST', body=True)

    def sync_with_ldap(self) -> dict:
        """
        Synchronize any user attribute changes in the configured AD/LDAP server with Mattermost.
        Must have manage_system permission.
        :return: LDAP sync info.
        """
        url = f"{self.api_url}/sync"
        self.reset()

        return self.request(url, request_type='POST')

    def test_ldap_configuration(self) -> dict:
        """
        Test the current AD/LDAP configuration to see if the AD/LDAP server can be contacted successfully.
        Must have manage_system permission.
        :return: LDAP test info.
        """
        url = f"{self.api_url}/test"
        self.reset()

        return self.request(url, request_type='POST')

    def migrate_id_ldap(self, toAttribute: str) -> dict:
        """
        Migrate LDAP IdAttribute to new value.
        Minimum server version: 5.26
        Must have manage_system permission.
        :param toAttribute: New IdAttribute value
        :return: Migration info.
        """
        url = f"{self.api_url}/migrateid"
        self.reset()
        self.add_application_json_header()

        if toAttribute is not None:
            self.add_to_json('toAttribute', toAttribute)

        return self.request(url, request_type='POST', body=True)
