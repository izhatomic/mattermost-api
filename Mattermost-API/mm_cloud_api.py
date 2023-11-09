from typing import Union, List, Dict
from Mattermost_Base import Base


class Cloud(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/cloud"

    def get_cloud_workspace_limits(self) -> dict:
        """
        Retrieve any cloud workspace limits applicable to this instance.

        Minimum server version: 7.0
        Must be authenticated and be licensed for Cloud.
        Note: This is intended for internal use and is subject to change.

        :return: Cloud workspace limits info.
        """

        url = f"{self.api_url}/limits"
        self.reset()

        return self.request(url, request_type='GET')
