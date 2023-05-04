from typing import Union, List, Dict
from Mattermost_Base import Base


class TermsOfService(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/users/"

    def records_user_action_custom_terms(self, user_id: str,
                                         serviceTermsId: str,
                                         accepted) -> dict:
        """
        Records user action when they accept or decline custom terms of service.
        Records the action in audit table. Updates user's last accepted terms of service ID
        if they accepted it.

        Minimum server version: 5.4
        Must be logged in as the user being acted on.
        :param user_id: User GUID
        :param serviceTermsId: terms of service ID on which the user is acting on
        :param accepted: true or false, indicates whether the user accepted or rejected the terms of service.
        :return: Terms of service action recorded successfully
        """

        url = f"{self.api_url}/{user_id}/terms_of_service"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('user_id', user_id)
        self.add_to_json('serviceTermsId', serviceTermsId)
        self.add_to_json('accepted', accepted)

        return self.request(url, request_type='POST', body=True)