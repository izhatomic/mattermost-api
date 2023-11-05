from typing import Union, List, Dict
from Mattermost_Base import Base


class Shared_channels(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/sharedchannels"

    def get_shrd_chnls_for_team(self, team_id: str,
                      page: int,
                      per_page: int) -> dict:
        """
        Get all shared channels for a team.

        Minimum server version: 5.50
        Must be authenticated.

        :param team_id: Team ID.
        :param page: Default: 0. The page to select.
        :param per_page: Default: 0. The number of sharedchannels per page.
        :return: Shared channels info.
        """

        url = f"{self.api_url}/{team_id}"
        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)

