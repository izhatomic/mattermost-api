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

    def complete_payment_setup_intent(self, stripe_setup_intent_id: str) -> dict:
        """
        Confirms the payment setup intent initiated when posting to /cloud/payment.

        Minimum server version: 5.28
        Must have manage_system permission and be licensed for Cloud.
        Note: This is intended for internal use and is subject to change.

        :param stripe_setup_intent_id: id of the payment setup intent
        :return: Policies count info.
        """

        url = f"{self.api_url}/confirm"

        self.reset()
        self.add_application_json_header()
        if stripe_setup_intent_id is not None:
            self.add_to_json('stripe_setup_intent_id', stripe_setup_intent_id)

        return self.request(url, request_type='POST')

    def get_cloud_customer(self) -> dict:
        """
        Retrieves the customer information for the Mattermost Cloud customer bound to this installation.

        Minimum server version: 5.28
        Must have manage_system permission and be licensed for Cloud.
        Note: This is intended for internal use and is subject to change.

        :return: Cloud customer info.
        """

        url = f"{self.api_url}/customer"
        self.reset()

        return self.request(url, request_type='GET')

    def update_cloud_customer(self,
                              name: str,
                              email: str,
                              contact_first_name: str,
                              contact_last_name: str,
                              num_employees: str) -> dict:
        """
        Updates the customer information for the Mattermost Cloud customer bound to this installation.

        Minimum server version: 5.29
        Must have manage_system permission and be licensed for Cloud.
        Note: This is intended for internal use and is subject to change.

        :param name: The name to update.
        :param email: The email to update.
        :param contact_first_name: The contact first name to update.
        :param contact_last_name: The contact last name to update.
        :param num_employees: The number of employees.
        :return: Cloud customer updating info.
        """
        url = f"{self.api_url}/customer"
        self.reset()
        self.add_application_json_header()
        if name is not None:
            self.add_to_json('name', name)
        if email is not None:
            self.add_to_json('email', email)
        if contact_first_name is not None:
            self.add_to_json('contact_first_name', contact_first_name)
        if contact_last_name is not None:
            self.add_to_json('contact_last_name', contact_last_name)
        if num_employees is not None:
            self.add_to_json('num_employees', num_employees)

        return self.request(url, request_type='PUT', body=True)
