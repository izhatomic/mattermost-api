from typing import Union, List, Dict
from Mattermost_Base import Base


class Intagration_Actions(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/actions/dialogs"

    def open_dialog(self, trigger_id: str
                    url: str
                    dialog: dict) -> dict:

    """
    Open an interactive dialog using a trigger ID provided by
    a slash command,or some other action payload.

    Minimum server version: 5.6
    No special permission.

    :param trigger_id: Trigger ID provided by other action
    :param url: The URL to send the submitted dialog payload to
    :param dialog: Post object to create
    :return: Dialog open succesful
    """

    url = f"{self.api_url}/open"

    self.reset()
    self.add_application_json_header()
    self.add_to_json('trigger_id', trigger_id)
    self.add_to_json('url', url)
    self.add_to_json('dialog', dialog)

    return self.request(url, request_type='POST', body=True)
