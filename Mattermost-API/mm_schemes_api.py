from typing import Union, List, Dict
from Mattermost_Base import Base


class Schemes(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/schemes"

    def get_the_schemes(self, scope: str,
                        page: int,
                        per_page: int) -> dict:
        """
        Get a page of schemes. Use the query parameters to modify
        the behaviour of this endpoint.

        Minimum server version: 5.50
        Must have manage_system permission.

        :param scope: Default: "". Limit the results returned to the provided scope,
        either team or channel.
        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of schemes per page.
        :return: Schemes list.
        """

        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        if scope is not None:
            self.add_to_json('scope', scope)
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)

    def create_a_scheme(self,
                        name: str,
                        description: str,
                        scope: str) -> dict:
        """
        Create a new scheme.

        Minimum server version: 5.50
        Must have manage_system permission.

        :param name: The name of the scheme.
        :param description: The description of the scheme.
        :param scope: The scope of the scheme ("team" or "channel").
        :return: Schemes creation info.
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('name', name)
        if description is not None:
            self.add_to_json('description', description)
        self.add_to_json('scope', scope)

        return self.request(url, request_type='GET', body=True)

    def get_a_scheme(self, scheme_id: str) -> dict:
        """
        Get a scheme from the provided scheme id.

        Minimum server version: 5.0
        Must have manage_system permission.

        :param scheme_id: Scheme GUID.
        :return: Schemes retrieval info.
        """
        url = f"{self.api_url}/{scheme_id}"
        self.reset()

        return self.request(url, request_type='GET')
