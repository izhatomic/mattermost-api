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
