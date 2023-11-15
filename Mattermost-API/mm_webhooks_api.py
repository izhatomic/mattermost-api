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

    def update_incoming_webhook(self,
                                hook_id: str,
                                id: str,
                                channel_id: str,
                                display_name: str,
                                description: str,
                                username: str,
                                icon_url: str) -> dict:
        """
        Update an incoming webhook given the hook id.

        manage_webhooks for system or manage_webhooks for the specific team or manage_webhooks for the channel.

        :param hook_id: Incoming Webhook GUID.
        :param id: Incoming Webhook GUID.
        :param channel_id: The ID of a public channel or private group that receives the webhook payloads.
        :param display_name: The display name for this incoming webhook.
        :param description: The description for this incoming webhook.
        :param username: The username this incoming webhook will post as.
        :param icon_url: The profile picture this incoming webhook will use when posting.
        :return: Webhook update info.
        """

        url = f"{self.api_url}/incoming/{hook_id}"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('id', id)
        self.add_to_json('channel_id', channel_id)
        self.add_to_json('display_name', display_name)
        self.add_to_json('description', description)
        if username is not None:
            self.add_to_json('username', username)
        if icon_url is not None:
            self.add_to_json('icon_url', icon_url)

        return self.request(url, request_type='PUT', body=True)

    def create_outgoing_webhook(self,
                                team_id: str,
                                channel_id: str,
                                creator_id: str,
                                description: str,
                                display_name: str,
                                trigger_words: list[str],
                                trigger_when: int,
                                callback_urls: list[str],
                                content_type: str) -> dict:
        """
        Create an outgoing webhook for a team.

        manage_webhooks for the team the webhook is in.
        manage_others_outgoing_webhooks for the team the webhook is in if the user is different than the requester.

        :param team_id: The ID of the team that the webhook watchs.
        :param channel_id: The ID of a public channel that the webhook watchs.
        :param creator_id: The ID of the owner of the webhook if different than the requester. Required in local mode.
        :param description: The description for this outgoing webhook.
        :param display_name: The display name for this outgoing webhook.
        :param trigger_words: List of words for the webhook to trigger on.
        :param trigger_when: When to trigger the webhook, 0 when a trigger word is present at all and 1
        if the message starts with a trigger word.
        :param callback_urls: The URLs to POST the payloads to when the webhook is triggered.
        :param content_type: Default: "application/x-www-form-urlencoded". The format to POST the data in,
        either application/json or application/x-www-form-urlencoded
        :return: Outgoing webhook creation info.
        """

        url = f"{self.api_url}/outgoing"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('team_id', team_id)
        if channel_id is not None:
            self.add_to_json('channel_id', channel_id)
        if creator_id is not None:
            self.add_to_json('creator_id', creator_id)
        if description is not None:
            self.add_to_json('description', description)
        self.add_to_json('display_name', display_name)
        self.add_to_json('trigger_words', trigger_words)
        if trigger_when is not None:
            self.add_to_json('trigger_when', trigger_when)
        self.add_to_json('callback_urls', callback_urls)
        if content_type is not None:
            self.add_to_json('content_type', content_type)

        return self.request(url, request_type='POST', body=True)

    def list_outgoing_webhooks(self,
                               page: int,
                               per_page: int,
                               team_id: str,
                               channel_id: str) -> dict:
        """
        Get a page of a list of outgoing webhooks. Optionally filter for
        a specific team or channel using query parameters.

        manage_webhooks for the system or manage_webhooks for the specific team/channel.

        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of hooks per page.
        :param team_id: The ID of the team to get hooks for.
        :param channel_id: The ID of the channel to get hooks for.
        :return: Outgoing webhook retrieval info.
        """

        url = f"{self.api_url}/outgoing"

        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)
        if team_id is not None:
            self.add_to_json('team_id', team_id)
        if channel_id is not None:
            self.add_to_json('channel_id', channel_id)

        return self.request(url, request_type='GET', body=True)

    def get_outgoing_webhook(self, hook_id: str) -> dict:
        """
        Get an outgoing webhook given the hook id.

        manage_webhooks for system or manage_webhooks for the specific team or manage_webhooks for the channel.

        :param hook_id: Outgoing webhook GUID.
        :return: Outgoing webhook retrieval info.
        """

        url = f"{self.api_url}/outgoing/{hook_id}"

        self.reset()

        return self.request(url, request_type='GET')

    def delete_outgoing_webhook(self, hook_id: str) -> dict:
        """
        Delete an outgoing webhook given the hook id.

        manage_webhooks for system or manage_webhooks for the specific team or manage_webhooks for the channel.

        :param hook_id: Outgoing webhook GUID.
        :return: Outgoing webhook deletion info.
        """

        url = f"{self.api_url}/outgoing/{hook_id}"

        self.reset()

        return self.request(url, request_type='DEL')

    def update_outgoing_webhook(self,
                                hook_id: str,
                                id: str,
                                channel_id: str,
                                display_name: str,
                                description: str) -> dict:
        """
        Update an outgoing webhook given the hook id.

        manage_webhooks for system or manage_webhooks for the specific team or manage_webhooks for the channel.

        :param hook_id: Outgoing Webhook GUID.
        :param id: Outgoing Webhook GUID.
        :param channel_id: The ID of a public channel or private group that receives the webhook payloads.
        :param display_name: The display name for this outgoing webhook.
        :param description: The description for this outgoing webhook.
        :return: Outgoing webhook update info.
        """

        url = f"{self.api_url}/incoming/{hook_id}"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('hook_id', hook_id)
        self.add_to_json('id', id)
        self.add_to_json('channel_id', channel_id)
        self.add_to_json('display_name', display_name)
        self.add_to_json('description', description)

        return self.request(url, request_type='PUT', body=True)
