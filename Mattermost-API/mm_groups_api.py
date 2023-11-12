from typing import Union, List, Dict
from Mattermost_Base import Base


class Cloud(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/groups"

    def delete_link_for_ldap_group(self,remote_id:str) ->dict:
        """
        Deletes a link for LDAP group.

        Minimum server version: 5.11
        Must have manage_system permission.

        :param remote_id: Group GUID.
        :return: LDAP group link deletion info.
        """
        url = f"{self.base_url}/ldap/groups/{remote_id}/link"
        self.reset()

        return self.request(url, request_type='DEL')

    def get_groups(self,
                   page: int,
                   per_page: int,
                   q: str,
                   include_member_count: bool,
                   not_associated_to_team: str,
                   not_associated_to_channel: str,
                   since: int,
                   filter_allow_reference: bool) -> dict:
        """
        Retrieve a list of all groups not associated to a particular channel or team.

        Minimum server version: 5.11

        not_associated_to_team OR not_associated_to_channel is required.
        If you use not_associated_to_team, you must be a team admin for that particular
        team (permission to manage that team).
        If you use not_associated_to_channel, you must be a channel admin for that particular
        channel (permission to manage that channel).
        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of groups per page.
        :param q: String to pattern match the name and display_name field.
        Will return all groups whose name and display_name field match any of the text.
        :param include_member_count: Boolean which adds the member_count attribute to
        each group JSON object
        :param not_associated_to_team: Team GUID which is used to return all
        the groups not associated to this team
        :param not_associated_to_channel: Group GUID which is used to return
        all the groups not associated to this channel
        :param since: Only return groups that have been modified since the given Unix
        timestamp (in milliseconds). All modified groups, including deleted and created
        groups, will be returned. Minimum server version: 5.24
        :param filter_allow_reference: Default: false. Boolean which filters the group
        entries with the allow_reference attribute set.
        :return: Group list retrieval info.
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)
        if q is not None:
            self.add_to_json('q', q)
        if include_member_count is not None:
            self.add_to_json('include_member_count', include_member_count)
        self.add_to_json('not_associated_to_team', not_associated_to_team)
        self.add_to_json('not_associated_to_channel', not_associated_to_channel)
        if since is not None:
            self.add_to_json('since', since)
        if filter_allow_reference is not None:
            self.add_to_json('filter_allow_reference', filter_allow_reference)

        return self.request(url, request_type='GET', body=True)

    def create_custom_group(self,
                            group: dict,
                            user_ids: list[str]) -> dict:
        """
        Create a custom type group.

        Minimum server version: 6.3
        Must have create_custom_group permission.
        :param group: Group object to create.
        :param user_ids: The user ids of the group members to add.
        :return: Group creation info.
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('group', group)
        self.add_to_json('user_ids', user_ids)

        return self.request(url, request_type='POST', body=True)

    def get_a_group(self, group_id: str) -> dict:

        """
        Get group from the provided group id string

        Minimum server version: 5.11
        Must have manage_system permission.
        :param group_id: Group GUID.
        :return: Group retrieval info.
        """
        url = f"{self.api_url}/{group_id}"
        self.reset()

        return self.request(url, request_type='GET')

    def deletes_custom_group(self, group_id: str) -> dict:
        """
        Soft deletes a custom group.

        Minimum server version: 6.3
        Must have custom_group_delete permission for the given group.
        :param group_id: The ID of the group.
        :return: Group deletion info.
        """
        url = f"{self.api_url}/{group_id}"
        self.reset()

        return self.request(url, request_type='DEL')

    def patch_a_group(self,
                      group_id: str,
                      name: str,
                      display_name: str,
                      description: str) -> dict:
        """
        Partially update a group by providing only the fields you want to update.
        Omitted fields will not be updated. The fields that can be updated are defined
        in the request body, all other provided fields will be ignored.

        Minimum server version: 5.11
        Must have manage_system permission.
        :param group_id: Group GUID.
        :param name: The name to update.
        :param display_name: The name to be displayed to update.
        :param description: Description to update.
        :return: Group patch info.
        """
        url = f"{self.api_url}/{group_id}/patch"
        self.reset()
        self.add_application_json_header()
        if name is not None:
            self.add_to_json('name', name)
        if display_name is not None:
            self.add_to_json('display_name', display_name)
        if description is not None:
            self.add_to_json('description', description)

        return self.request(url, request_type='PUT', body=True)

    def restore_previously_deleted_group(self, group_id: str) -> dict:
        """
        Restores a previously deleted custom group, allowing it to be used normally.
        May not be used with LDAP groups.

        Minimum server version: 7.7
        Permissions Must have restore_custom_group permission for the given group.
        :param group_id: Group GUID.
        :return: Group restoration info.
        """
        url = f"{self.api_url}/{group_id}/restore"
        self.reset()

        return self.request(url, request_type='POST')
