from typing import Union, List, Dict
from Mattermost_Base import Base


class Plugins(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/plugins"

    def upload_plugin(self,
                      plugin:str,
                      force:str) -> dict:
        """
        Upload a plugin that is contained within a compressed .tar.gz file.
        Plugins and plugin uploads must be enabled in the server's config settings.

        Minimum server version: 4.4
        Must have manage_system permission.

        :param plugin: The plugin image to be uploaded.
        :param force: Set to 'true' to overwrite a previously installed plugin with the same ID.
        :return: Plugin upload info.
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('plugin', plugin)
        if force is not None:
            self.add_to_json('force', force)

        return self.request(url, request_type='POST', body=True)

