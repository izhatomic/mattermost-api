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
