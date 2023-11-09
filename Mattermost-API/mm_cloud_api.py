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

    def get_cloud_products(self) -> dict:
        """
        Retrieve a list of all products that are offered for Mattermost Cloud.

        Minimum server version: 5.28
        Must be logged in as the user or have the manage_system permission.
        Note: This is intended for internal use and is subject to change.

        :return: Cloud products info.
        """

        url = f"{self.api_url}/products"
        self.reset()

        return self.request(url, request_type='GET')

    def create_customer_setup_payment_intent(self) -> dict:
        """
        Creates a customer setup payment intent for the given Mattermost cloud installation.

        Minimum server version: 5.28
        Must have manage_system permission and be licensed for Cloud.
        Note:: This is intended for internal use and is subject to change.

        :return: Payment setup info.
        """

        url = f"{self.api_url}/payment"
        self.reset()

        return self.request(url, request_type='POST')
