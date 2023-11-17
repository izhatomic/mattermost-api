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

    def delete_a_scheme(self, scheme_id: str) -> dict:
        """
        Soft deletes a scheme, by marking the scheme
        as deleted in the database.

        Minimum server version: 5.0
        Must have manage_system permission.

        :param scheme_id: ID of the scheme to delete.
        :return: Schemes deletion info.
        """
        url = f"{self.api_url}/{scheme_id}"
        self.reset()

        return self.request(url, request_type='DEL')

    def patch_a_scheme(self, scheme_id: str,
                       name: str,
                       description: str) -> dict:
        """
        Partially update a scheme by providing only the fields you want to update.
        Omitted fields will not be updated.
        The fields that can be updated are defined in the request body,
        all other provided fields will be ignored.

        Minimum server version: 5.0
        manage_system permission is required.

        :param scheme_id: Scheme GUID.
        :param name: The human readable name of the scheme.
        :param description: The description of the scheme.
        :return: Schemes deletion info.
        """
        url = f"{self.api_url}/{scheme_id}/patch"
        self.reset()
        self.add_application_json_header()
        if name is not None:
            self.add_to_json('name', name)
        if description is not None:
            self.add_to_json('description', description)

        return self.request(url, request_type='PUT', body=True)

    def get_a_pg_of_tms_use_scheme(self, scheme_id: str,
                                   page: int,
                                   per_page: int) -> dict:
        """
        Get a page of teams which use this scheme.
        The provided Scheme ID should be for a Team-scoped Scheme.
        Use the query parameters to modify the behaviour of this endpoint.

        Minimum server version: 5.0
        manage_system permission is required.

        :param scheme_id: Scheme GUID.
        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of teams per page.
        :return: Team list retrieval info.
        """
        url = f"{self.api_url}/{scheme_id}/teams"
        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)

    def get_a_pg_of_chnls_use_scheme(self,
                                     scheme_id: str,
                                     page: int,
                                     per_page: int) -> dict:
        """
        Get a page of channels which use this scheme.
        The provided Scheme ID should be for a Channel-scoped Scheme.
        Use the query parameters to modify the behaviour of this endpoint.

        Minimum server version: 5.0
        manage_system permission is required.

        :param scheme_id: Scheme GUID.
        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of channels per page.
        :return: Channel list retrieval info.
        """
        url = f"{self.api_url}/{scheme_id}/channels"
        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)
