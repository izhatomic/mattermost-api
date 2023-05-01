from typing import Union, List, Dict
from Mattermost_Base import Base


class Compliance(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/compliance"

    def create_report(self):
        """
        Create and save a compliance report.

        Must have manage_system permission.

        :return: Compliance report creation successfull
        """

        url = f"{self.api_url}/reports"

        self.reset()

        return self.request(url, request_type='POST')

    def get_reports(self, page: int, per_page: int) -> dict:
        """
        Get a list of compliance reports previously created by page,
        selected with page and per_page query parameters.

        Must have manage_system permission.

        :param page: The page to select.
        :param per_page: The number of reports per page.
        :return: Compliance reports retrieval successful
        """

        url = f"{self.api_url}/reports"

        self.reset()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET')

