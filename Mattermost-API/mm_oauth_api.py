from typing import Union, List, Dict
from Mattermost_Base import Base


class Oauth(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/oauth/apps"

    def register_oauth_app(self,
                           name: str,
                           description: str,
                           icon_url: str,
                           callback_urls: list[str],
                           homepage: str,
                           is_trusted: bool) -> dict:
        """
        Register an OAuth 2.0 client application with Mattermost as the service provider.
        Must have manage_oauth permission.
        :param name: The name of the client application.
        :param description: A short description of the application.
        :param icon_url: A URL to an icon to display with the application.
        :param callback_urls: A list of callback URLs for the appliation.
        :param homepage: A link to the website of the application.
        :param is_trusted: Set this to true to skip asking users for permission.
        :return: App registration info.
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('name', name)
        self.add_to_json('description', description)
        if icon_url is not None:
            self.add_to_json('icon_url', icon_url)
        self.add_to_json('callback_urls', callback_urls)
        self.add_to_json('homepage', homepage)
        if is_trusted is not None:
            self.add_to_json('is_trusted', is_trusted)

        return self.request(url, request_type='POST', body=True)

    def get_oauth_apps(self,
                       page: int,
                       per_page: int) -> dict:
        """
        Get a page of OAuth 2.0 client applications registered with Mattermost.
        With manage_oauth permission, the apps registered by the logged in user are returned.
        With manage_system_wide_oauth permission, all apps regardless of creator are returned.
        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of apps per page.
        :return: OAuth list retrieval info.
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)

    def get_an_oauth_app(self,
                         app_id: str) -> dict:
        """
        Get an OAuth 2.0 client application registered with Mattermost.
        If app creator, must have mange_oauth permission otherwise manage_system_wide_oauth
        permission is required.
        :param app_id: Application client id.
        :return: App retrieval info.
        """
        url = f"{self.api_url}/{app_id}"
        self.reset()

        return self.request(url, request_type='GET')

    def update_an_oauth_app(self,
                            app_id: str,
                            id: str,
                            name: str,
                            description: str,
                            icon_url: str,
                            callback_urls: list[str],
                            homepage: str,
                            is_trusted: bool) -> dict:
        """
        Get an OAuth 2.0 client application registered with Mattermost.
        If app creator, must have mange_oauth permission otherwise manage_system_wide_oauth
        permission is required.
        :param app_id: Application client id.
        :param id: The id of the client application.
        :param name: The name of the client application.
        :param description: A short description of the application.
        :param icon_url: A URL to an icon to display with the application.
        :param callback_urls: A list of callback URLs for the appliation.
        :param homepage: A link to the website of the application.
        :param is_trusted: Set this to true to skip asking users for permission.
        It will be set to false if value is not provided.
        :return: App retrieval info.
        """
        url = f"{self.api_url}/{app_id}"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('id', id)
        self.add_to_json('name', name)
        self.add_to_json('description', description)
        if icon_url is not None:
            self.add_to_json('icon_url', icon_url)
        self.add_to_json('callback_urls', callback_urls)
        self.add_to_json('homepage', homepage)
        if is_trusted is not None:
            self.add_to_json('is_trusted', is_trusted)

        return self.request(url, request_type='PUT', body=True)

    def delete_an_oauth_app(self, app_id: str) -> dict:
        """
        Delete and unregister an OAuth 2.0 client application
        If app creator, must have mange_oauth permission otherwise manage_system_wide_oauth
        permission is required.
        :param app_id: Application client id.
        :return: App deletion info.
        """
        url = f"{self.api_url}/{app_id}"
        self.reset()

        return self.request(url, request_type='DEL')

    def regenerate_oauth_app_secret(self, app_id: str) -> dict:
        """
        Regenerate the client secret for an OAuth 2.0 client application registered with Mattermost.
        If app creator, must have mange_oauth permission otherwise manage_system_wide_oauth
        permission is required.
        :param app_id: Application client id.
        :return: Secret regeneration info.
        """
        url = f"{self.api_url}/{app_id}/regen_secret"
        self.reset()

        return self.request(url, request_type='POST')

    def get_info_on_oauth_app(self, app_id: str) -> dict:
        """
        Get public information about an OAuth 2.0 client application registered with Mattermost.
        The application's client secret will be blanked out.
        Must be authenticated.
        :param app_id: Application client id.
        :return: App retrieval info.
        """
        url = f"{self.api_url}/{app_id}/info"
        self.reset()

        return self.request(url, request_type='GET')
