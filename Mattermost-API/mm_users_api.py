from typing import Union, List, Dict
from Mattermost_Base import Base


class Uploads(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/users"

    def login_to_mattermost_server(self,
                                   id: str = None,
                                   login_id: str = None,
                                   token: str = None,
                                   device_id: str = None,
                                   ldap_only: str = None,
                                   password: str = None) -> dict:
        """
        Logins to Mattermost server.

        No permission required

        :param id: User ID for authentication.
        :param login_id: User login_id for authentication.
        :param token: User token for authentication.
        :param device_id: User device_id for authentication.
        :param ldap_only: User ldap_only for authentication.
        :param password: User password for authentication.
        :return: User login info.
        """

        url = f"{self.api_url}/login"

        self.reset()
        self.add_application_json_header()
        if id is not None:
            self.add_to_json('id', id)
        if login_id is not None:
            self.add_to_json('login_id', login_id)
        if token is not None:
            self.add_to_json('token', token)
        if device_id is not None:
            self.add_to_json('device_id', device_id)
        if ldap_only is not None:
            self.add_to_json('ldap_only', ldap_only)
        if password is not None:
            self.add_to_json('password', password)

        return self.request(url, request_type='POST', body=True)

    def autologin_to_mm_server_using_cws_token(self,
                                               login_id: str = None,
                                               cws_token: str = None) -> dict:
        """
        CWS stands for Customer Web Server which is the cloud service used to manage cloud instances.

        A Cloud license is required

        :param login_id: User login_id for authentication.
        :param cws_token: User cws_token for authentication.
        :return: User login info.
        """

        url = f"{self.api_url}/login/cws"

        self.reset()
        self.add_application_json_header()
        if login_id is not None:
            self.add_to_json('login_id', login_id)
        if cws_token is not None:
            self.add_to_json('cws_token', cws_token)

        return self.request(url, request_type='POST', body=True)

    def logout_from_mm_server(self)->dict:
        """
        Logout from the Mattermost server.

        An active session is required

        :return: User logout info.
        """

        url = f"{self.api_url}/logout"

        self.reset()

        return self.request(url, request_type='POST')

    def create_user(self,
                    email: str,
                    username: str,
                    t: str = None,
                    iid: str = None,
                    first_name: str = None,
                    last_name: str = None,
                    nickname: str = None,
                    auth_data: str = None,
                    auth_service: str = None,
                    password: str = None,
                    locale: str = None,
                    props: dict = None,
                    notify_props: str = None) -> dict:
        """
        Create a new user on the system. Password is required for email login.
        For other authentication types such as LDAP or SAML, auth_data and auth_service fields are required.

        No permission required for creating email/username accounts on an open server.
        Auth Token is required for other authentication types such as LDAP or SAML.

        :param email: User email to be created.
        :param username: User username to be created.
        :param t: Token id from an email invitation.
        :param iid: Token id from an invitation link.
        :param first_name: User first_name to be created.
        :param last_name: User last_name to be created.
        :param nickname: User nickname to be created.
        :param auth_data: Service-specific authentication data, such as email address.
        :param auth_service: The authentication service, one of
        "email", "gitlab", "ldap", "saml", "office365", "google", and "".
        :param password: The password used for email authentication.
        :param locale: User locale to be created.
        :param props: User props to be created.
        :param notify_props: User notify_props to be created.
        :return: User creation info.
        """

        url = f"{self.api_url}"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('email', email)
        self.add_to_json('username', username)
        if t is not None:
            self.add_to_json('t', t)
        if iid is not None:
            self.add_to_json('iid', iid)
        if first_name is not None:
            self.add_to_json('first_name', first_name)
        if last_name is not None:
            self.add_to_json('last_name', last_name)
        if nickname is not None:
            self.add_to_json('nickname', nickname)
        if auth_data is not None:
            self.add_to_json('auth_data', auth_data)
        if auth_service is not None:
            self.add_to_json('auth_service', auth_service)
        if password is not None:
            self.add_to_json('password', password)
        if locale is not None:
            self.add_to_json('locale', locale)
        if props is not None:
            self.add_to_json('props', props)
        if notify_props is not None:
            self.add_to_json('notify_props', notify_props)

        return self.request(url, request_type='POST', body=True)

    def get_users(self,
                  page: int = None,
                  per_page: int = None,
                  in_team: str = None,
                  not_in_team: str = None,
                  in_channel: str = None,
                  not_in_channel: str = None,
                  in_group: str = None,
                  group_constrained: bool = None,
                  without_team: bool = None,
                  active: bool = None,
                  inactive: bool = None,
                  role: str = None,
                  sort: str = None,
                  roles: str = None,
                  channel_roles: str = None,
                  team_roles: str = None) -> dict:
        """
        Get a page of a list of users. Based on query string parameters,
        select users from a team, channel, or select users not in a specific channel.
        Since server version 4.0, some basic sorting is available using the sort query parameter.
        Sorting is currently only supported when selecting users on a team.

        Requires an active session and (if specified) membership to the channel or team being selected from.

        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of users per page. There is a maximum limit of 200 users per page.
        :param in_team: The ID of the team to get users for.
        :param not_in_team: The ID of the team to exclude users for. Must not be used with "in_team" query parameter.
        :param in_channel: The ID of the channel to get users for.
        :param not_in_channel: The ID of the channel to exclude users for.
        Must be used with "in_channel" query parameter.
        :param in_group: The ID of the group to get users for. Must have manage_system permission.
        :param group_constrained: When used with not_in_channel or not_in_team,
        returns only the users that are allowed to join the channel or team based on its group constrains.
        :param without_team: Whether or not to list users that are not on any team.
        This option takes precendence over in_team, in_channel, and not_in_channel.
        :param active: Whether or not to list only users that are active.
        This option cannot be used along with the inactive option.
        :param inactive: Whether or not to list only users that are deactivated.
        This option cannot be used along with the active option.
        :param role: Returns users that have this role.
        :param sort: Sort is only available in conjunction with certain options below.
        The paging parameter is also always available.
        in_team Can be "", "last_activity_at" or "create_at". When left blank, sorting is done by username.
        Minimum server version: 4.0
        in_channel Can be "", "status". When left blank, sorting is done by username. status will sort by User's
        current status (Online, Away, DND, Offline), then by Username. Minimum server version: 4.7
        in_group Can be "", "display_name". When left blank, sorting is done by username.
        display_name will sort alphabetically by user's display name. Minimum server version: 7.7
        :param roles: Comma separated string used to filter users based on any of the specified system roles
        Example: ?roles=system_admin,system_user will return users that are either system admins or system users
        Minimum server version: 5.26
        :param channel_roles: Comma separated string used to filter users based on any of the specified channel roles,
        can only be used in conjunction with in_channel
        Example: ?in_channel=4eb6axxw7fg3je5iyasnfudc5y&channel_roles=channel_user will return users that are only
        channel users and not admins or guests. Minimum server version: 5.26
        :param team_roles: Comma separated string used to filter users based on any of the specified team roles,
        can only be used in conjunction with in_team. Example: ?in_team=4eb6axxw7fg3je5iyasnfudc5y&team_roles=team_user
        will return users that are only team users and not admins or guests. Minimum server version: 5.26
        :return: User page retrieval info.
        """

        url = f"{self.api_url}"

        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)
        if in_team is not None:
            self.add_to_json('in_team', in_team)
        if not_in_team is not None:
            self.add_to_json('not_in_team', not_in_team)
        if in_channel is not None:
            self.add_to_json('in_channel', in_channel)
        if not_in_channel is not None:
            self.add_to_json('not_in_channel', not_in_channel)
        if in_group is not None:
            self.add_to_json('in_group', in_group)
        if group_constrained is not None:
            self.add_to_json('group_constrained', group_constrained)
        if without_team is not None:
            self.add_to_json('without_team', without_team)
        if active is not None:
            self.add_to_json('active', active)
        if inactive is not None:
            self.add_to_json('inactive', inactive)
        if role is not None:
            self.add_to_json('role', role)
        if sort is not None:
            self.add_to_json('sort', sort)
        if roles is not None:
            self.add_to_json('roles', roles)
        if channel_roles is not None:
            self.add_to_json('channel_roles', channel_roles)
        if team_roles is not None:
            self.add_to_json('team_roles', team_roles)

        return self.request(url, request_type='GET', body=True)
