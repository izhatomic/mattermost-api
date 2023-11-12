from typing import Union, List, Dict
from Mattermost_Base import Base


class Cloud(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/groups"

    def delete_link_for_ldap_group(self,remote_id:str) ->dict:
        """
        Deletes a link for LDAP group.

        Minimum server version: 5.11
        Must have manage_system permission.

        :param remote_id: Group GUID.
        :return: Cloud workspace limits info.
        """
        url = f"{self.base_url}/ldap/groups/{remote_id}/link"
        self.reset()

        return self.request(url, request_type='DEL')


