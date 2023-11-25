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
        :param auth_data: User auth_data to be created.
        :param auth_service: User auth_service to be created.
        :param password: User password to be created.
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
