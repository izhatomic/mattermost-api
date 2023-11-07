from typing import Union, List, Dict
from Mattermost_Base import Base


class Jobs(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/jobs"

    def get_the_jobs(self,
                     page: int,
                     per_page: int) -> dict:
        """
        Get a page of jobs. Use the query parameters to
        modify the behaviour of this endpoint.

        Minimum server version: 4.1
        Must have manage_jobs permission.

        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of jobs per page.
        :return: Jobs list retrieval info.
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)
