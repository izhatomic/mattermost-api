from typing import Union, List, Dict
from Mattermost_Base import Base


class DataRetention(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/data_retention"

    def get_policies_applied_to_user_teams(self, user_id: str,
                                           page: int,
                                           per_page: int) -> dict:
        """
        Gets the policies which are applied to the all of the teams
        to which a user belongs.

        Minimum server version: 5.35
        Must be logged in as the user or have the manage_system permission.
        Requires an E20 license.

        :param user_id:	The ID of the user. This can also be "me" which will
        point to the current user.
        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of policies per page.
        There is a maximum limit of 200 per page.
        :return: Retention policy teams info.
        """
        url = f"{self.base_url}/users/{user_id}/data_retention/team_policies"

        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)

    def get_policies_applied_to_user_chnls(self,
                                           user_id: str,
                                           page: int,
                                           per_page: int) -> dict:
        """
        Gets the policies which are applied to the all of the channels to which a user belongs.

        Minimum server version: 5.35
        Must be logged in as the user or have the manage_system permission.
        Requires an E20 license.

        :param user_id:	The ID of the user. This can also be "me" which will point to the current user.
        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of policies per page. There is a maximum limit of 200 per page.
        :return: Retention policy channels info.
        """
        url = f"{self.base_url}/users/{user_id}/data_retention/channel_policies"
        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)

    def get_global_data_retention_policy(self) -> dict:
        """
        Gets the current global data retention policy details from the server, including what data should be purged and the cutoff times for each data type that should be purged.

        Minimum server version: 4.3
        Requires an active session but no other permissions.
        Requires an E20 license.

        :return: Global data retention policy info.
        """
        url = f"{self.api_url}/policy"
        self.reset()

        return self.request(url, request_type='GET')

    def get_number_of_granular_drp(self) -> dict:
        """
        Gets the number of granular (i.e. team or channel-specific)
        data retention policies from the server.

        Minimum server version: 5.35
        Must have the sysconsole_read_compliance_data_retention permission.
        Requires an E20 license.

        :return: Policies count info.
        """
        url = f"{self.api_url}/policies_count"
        self.reset()

        return self.request(url, request_type='GET')

    def get_the_granular_drp(self,
                         page: int,
                         per_page: int) -> dict:
        """
        Gets details about the granular (i.e. team or channel-specific)
        data retention policies from the server.

        Minimum server version: 5.35
        Must have the sysconsole_read_compliance_data_retention permission.
        Requires an E20 license.

        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of policies per page.
        There is a maximum limit of 200 per page.
        :return: Policies count info.
        """
        url = f"{self.api_url}/policies"
        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)

    def create_new_granular_drp(self,
                                display_name: str,
                                post_duration: int,
                                team_ids: list[str],
                                channel_ids: list[str]) -> dict:
        """
        Creates a new granular data retention policy with the specified display name and post duration.

        Minimum server version: 5.35
        Must have the sysconsole_write_compliance_data_retention permission.
        Requires an E20 license.

        :param display_name: The display name for this retention policy.
        :param post_duration: The number of days a message will be retained before being deleted by this policy. If this value is less than 0, the policy has infinite retention (i.e. messages are never deleted).
        :param team_ids: The IDs of the teams to which this policy should be applied.
        :param channel_ids: The IDs of the channels to which this policy should be applied.
        :return: Policies count info.
        """
        url = f"{self.api_url}/policies"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('display_name', display_name)
        self.add_to_json('post_duration', post_duration)
        if team_ids is not None:
            self.add_to_json('team_ids', team_ids)
        if channel_ids is not None:
            self.add_to_json('channel_ids', channel_ids)

        return self.request(url, request_type='POST', body=True)

    def get_a_granular_drp(self, policy_id: str) -> dict:
        """
        Gets details about a granular data retention policies by ID.

        Minimum server version: 5.35
        Must have the sysconsole_read_compliance_data_retention permission.
        Requires an E20 license.

        :param policy_id: The ID of the granular retention policy.
        :return: Policies retention info.
        """
        url = f"{self.api_url}/policies/{policy_id}"
        self.reset()

        return self.request(url, request_type='POST')

    def patch_a_granular_drp(self,
                             policy_id: str,
                             display_name: str,
                             post_duration: int,
                             team_ids: list[str],
                             channel_ids: list[str]) -> dict:
        """
        Patches (i.e. replaces the fields of) a granular data retention policy. If any fields are omitted, they will not be changed.

        Minimum server version: 5.35
        Must have the sysconsole_write_compliance_data_retention permission.
        Requires an E20 license.

        :param policy_id: The ID of the granular retention policy.
        :param display_name: The display name for this retention policy.
        :param post_duration: The number of days a message will be retained before being deleted by this policy. If this value is less than 0, the policy has infinite retention (i.e. messages are never deleted).
        :param team_ids: The IDs of the teams to which this policy should be applied.
        :param channel_ids: The IDs of the channels to which this policy should be applied.
        :return: Patching policies retention info.
        """
        url = f"{self.api_url}/policies/{policy_id}"
        self.reset()
        self.add_application_json_header()
        if display_name is not None:
            self.add_to_json('display_name', display_name)
        if post_duration is not None:
            self.add_to_json('post_duration', post_duration)
        if team_ids is not None:
            self.add_to_json('team_ids', team_ids)
        if channel_ids is not None:
            self.add_to_json('channel_ids', channel_ids)

        return self.request(url, request_type='PATCH', body=True)

    def delete_granular_drp(self, policy_id: str) -> dict:
        """
        Deletes a granular data retention policy.

        Minimum server version: 5.35
        Must have the sysconsole_write_compliance_data_retention permission.
        Requires an E20 license.

        :param policy_id: The ID of the granular retention policy.
        :return: Retention policy deletion info.
        """
        url = f"{self.api_url}/policies/{policy_id}"
        self.reset()

        return self.request(url, request_type='DEL')

    def get_teams_for_granular_drp(self,
                                   policy_id: str,
                                   page: int,
                                   per_page: int) -> dict:
        """
        Gets the teams to which a granular data retention policy is applied.

        Minimum server version: 5.35
        Must have the sysconsole_read_compliance_data_retention permission.
        Requires an E20 license.

        :param policy_id: The ID of the granular retention policy.
        :param page: Default: 0.The page to select.
        :param per_page: Default: 60. The number of teams per page. There is a maximum limit of 200 per page.
        :return: Teams for retention policy info.
        """

        url = f"{self.api_url}/policies/{policy_id}/teams"
        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='DEL', body=True)

    def add_teams_to_granular_drp(self,
                                  policy_id: str,
                                  teams_ids: list[str]) -> dict:
        """
        Adds teams to a granular data retention policy.

        Minimum server version: 5.35
        Must have the sysconsole_write_compliance_data_retention permission.
        Requires an E20 license.

        :param policy_id: The ID of the granular retention policy.
        :param teams_ids: The IDs of the teams to add to the policy.
        :return: Teams addition info.
        """
        url = f"{self.api_url}/policies/{policy_id}/teams"
        self.reset()
        self.add_application_json_header()
        if teams_ids is not None:
            self.add_to_json('teams_ids', teams_ids)

        return self.request(url, request_type='POST', body=True)

    def delete_teams_from_granular_drp(self,
                                       policy_id: str,
                                       teams_ids: list[str]) -> dict:
        """
        Delete teams from a granular data retention policy.

        Minimum server version: 5.35
        Must have the sysconsole_write_compliance_data_retention permission.

        :param policy_id: The ID of the granular retention policy.
        :param teams_ids: The IDs of the teams to remove from the policy.
        :return: Teams addition info.
        """
        url = f"{self.api_url}/policies/{policy_id}/teams"
        self.reset()
        self.add_application_json_header()
        if teams_ids is not None:
            self.add_to_json('teams_ids', teams_ids)

        return self.request(url, request_type='DEL', body=True)

    def search_for_teams_in_granular_drp(self, policy_id: str, term: str) -> dict:
        """
        Searches for the teams to which a granular data retention policy is applied.

        Minimum server version: 5.35
        Must have the sysconsole_read_compliance_data_retention permission.

        :param policy_id: The ID of the granular retention policy.
        :param term: The search term to match against the name or display name of teams
        :return: Teams retrieval info.
        """
        url = f"{self.api_url}/policies/{policy_id}/teams/search"
        self.reset()
        self.add_application_json_header()
        if term is not None:
            self.add_to_json('term', term)

        return self.request(url, request_type='POST', body=True)
