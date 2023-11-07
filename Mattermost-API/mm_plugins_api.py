from typing import Union, List, Dict
from Mattermost_Base import Base


class Plugins(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/plugins"

    def upload_plugin(self,
                      plugin: str,
                      force: str) -> dict:
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

    def get_plugins(self) -> dict:
        """
        Get a list of inactive and a list of active plugin manifests.
        Plugins must be enabled in the server's config settings.

        Minimum server version: 4.4
        Must have manage_system permission.

        :return: Plugin retrieval info.
        """
        url = f"{self.api_url}/"
        self.reset()

        return self.request(url, request_type='GET')

    def install_plugin_from_url(self,
                                plugin_download_url: str,
                                force: str) -> dict:
        """
        Supply a URL to a plugin compressed in a .tar.gz file.
        Plugins must be enabled in the server's config settings.

        Minimum server version: 5.14
        Must have manage_system permission.

        :return: Plugin installation info.
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('plugin_download_url', plugin_download_url)
        if force is not None:
            self.add_to_json('force', force)

        return self.request(url, request_type='POST', body=True)

    def remove_plugin(self, plugin_id: str) -> dict:
        """
        Remove the plugin with the provided ID from the server.
        All plugin files are deleted.
        Plugins must be enabled in the server's config settings.

        Minimum server version: 4.4
        Must have manage_system permission.

        :param plugin_id: Id of the plugin to be removed
        :return: Plugin removal info.
        """
        url = f"{self.api_url}/{plugin_id}"
        self.reset()

        return self.request(url, request_type='DEL')

    def enable_plugin(self, plugin_id: str) -> dict:
        """
        Enable a previously uploaded plugin.
        Plugins must be enabled in the server's config settings.

        Minimum server version: 4.4
        Must have manage_system permission.

        :param plugin_id: Id of the plugin to be enabled.
        :return: Plugin state info.
        """
        url = f"{self.api_url}/{plugin_id}/enable"
        self.reset()

        return self.request(url, request_type='POST')

    def disable_plugin(self, plugin_id: str) -> dict:
        """
        Disable a previously enabled plugin.
        Plugins must be enabled in the server's config settings.

        Minimum server version: 4.4
        Must have manage_system permission.

        :param plugin_id: Id of the plugin to be disabled.
        :return: Plugin state info.
        """
        url = f"{self.api_url}/{plugin_id}/disable"
        self.reset()

        return self.request(url, request_type='POST')
