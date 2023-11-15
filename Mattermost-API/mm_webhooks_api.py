from typing import Union, List, Dict
from Mattermost_Base import Base


class Webhooks(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/hooks"

    def create_incoming_webhook(self,
                                channel_id: str,
                                user_id: str,
                                display_name: str,
                                description: str,
                                username: str,
                                icon_url: str) -> dict:
        """
        Create an incoming webhook for a channel.

        manage_webhooks for the team the webhook is in.
        manage_others_incoming_webhooks for the team the webhook is in if the user is different
        than the requester.

        :param channel_id: The ID of a public channel or private group that receives the webhook payloads..
        :param user_id: The ID of the owner of the webhook if different than the requester. Required for local mode.
        :param display_name: The display name for this incoming webhook
        :param description: The description for this incoming webhook
        :param username: The username this incoming webhook will post as.
        :param icon_url: The profile picture this incoming webhook will use when posting.
        :return: Incoming webhook creation info.
        """

        url = f"{self.api_url}/incoming"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('channel_id', channel_id)
        if user_id is not None:
            self.add_to_json('user_id', user_id)
        if display_name is not None:
            self.add_to_json('display_name', display_name)
        if description is not None:
            self.add_to_json('description', description)
        if username is not None:
            self.add_to_json('username', username)
        if icon_url is not None:
            self.add_to_json('icon_url', icon_url)

        return self.request(url, request_type='POST', body=True)

    def list_incoming_webhooks(self,
                               page: int,
                               per_page: int,
                               team_id: str) -> dict:
        """
        Get a page of a list of incoming webhooks. Optionally filter for a specific team using query parameters.

        manage_webhooks for the system or manage_webhooks for the specific team.

        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of hooks per page.
        :param team_id: The ID of the team to get hooks for.
        :return: Incoming webhook retreival info.
        """

        url = f"{self.api_url}/incoming"

        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)
        if team_id is not None:
            self.add_to_json('team_id', team_id)

        return self.request(url, request_type='GET', body=True)

    def get_incoming_webhook(self, hook_id: str) -> dict:
        """
        Get an incoming webhook given the hook id.

        manage_webhooks for system or manage_webhooks for the specific team or manage_webhooks for the channel.

        :param hook_id: Incoming Webhook GUID.
        :return: Webhook retrieval info.
        """

        url = f"{self.api_url}/incoming/{hook_id}"

        self.reset()

        return self.request(url, request_type='GET')

    def delete_incoming_webhook(self, hook_id: str) -> dict:
        """
        Delete an incoming webhook given the hook id.

        manage_webhooks for system or manage_webhooks for the specific team or manage_webhooks for the channel.

        :param hook_id: Incoming Webhook GUID.
        :return: Webhook deletion info.
        """

        url = f"{self.api_url}/incoming/{hook_id}"

        self.reset()

        return self.request(url, request_type='DEL')
