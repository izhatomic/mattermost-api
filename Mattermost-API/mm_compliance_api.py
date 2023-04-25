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

        :return:Compliance report creation successfull
        """

        url = f"{self.api_url}/reports"

        self.reset()

        return self.request(url, request_type='POST', body=True)
