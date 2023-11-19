from typing import Union, List, Dict
from Mattermost_Base import Base


class Bots(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/bots"

    def convert_user_into_bot(self, user_id: str) -> dict:
        """
        Convert a user into a bot.

        Minimum server version: 5.26

        Must have manage_system permission.

        :param user_id: User GUID
        :return: User conversion info
        """

        url = f"{self.base_url}/users/{user_id}/convert_to_bot"

        self.reset()

        return self.request(url, request_type='POST')

    def create_bot(self,
                   username: str,
                   display_name: str = None,
                   description: str = None) -> dict:
        """
        Create a new bot account on the system. Username is required.

        Must have create_bot permission.

        Minimum server version: 5.10

        :param username: Bot's name
        :param display_name: Bot's display name
        :param description: Bot's description
        :return: Bot creation info
        """

        url = f"{self.api_url}"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('username', username)
        if display_name is not None:
            self.add_to_json('display_name', display_name)
        if description is not None:
            self.add_to_json('description', description)

        return self.request(url, request_type='POST', body=True)

    def get_bots(self,
                 page: int = None,
                 per_page: int = None,
                 include_deleted: bool = None,
                 only_orphaned: bool = None) -> dict:

        """
        Get a page of a list of bots.

        Must have read_bots permission for bots you are managing, and read_others_bots permission for bots
        others are managing.

        Minimum server version: 5.10

        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of users per page. There is a maximum limit of 200 users per page.
        :param include_deleted: If deleted bots should be returned.
        :param only_orphaned: When true, only orphaned bots will be returned.
        A bot is consitered orphaned if it's owner has been deactivated.
        :return: Bot creation info
        """

        url = f"{self.api_url}"

        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)
        if include_deleted is not None:
            self.add_to_json('include_deleted', include_deleted)
        if only_orphaned is not None:
            self.add_to_json('only_orphaned', only_orphaned)

        return self.request(url, request_type='GET', body=True)

    def patch_bot(self,
                  bot_user_id: str,
                  username: str,
                  display_name: str = None,
                  description: str = None) -> dict:

        """
        Partially update a bot by providing only the fields you want to update.
        Omitted fields will not be updated.
        The fields that can be updated are defined in the request body, all other provided fields will be ignored.

        Must have manage_bots permission.
        Minimum server version: 5.10

        :param bot_user_id: Bot user ID.
        :param username: Bot's name.
        :param display_name: Bot's display name.
        :param description: Bot's name.
        A bot is consitered orphaned if it's owner has been deactivated.
        :return: Bot patch info
        """

        url = f"{self.api_url}/{bot_user_id}"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('username', username)
        if display_name is not None:
            self.add_to_json('display_name', display_name)
        if description is not None:
            self.add_to_json('description', description)

        return self.request(url, request_type='PUT', body=True)

    def get_bot(self,
                bot_user_id: str,
                include_deleted: bool = None) -> dict:

        """
        Get a bot specified by its bot id.

        Must have read_bots permission for bots you are managing,
        and read_others_bots permission for bots others are managing.

        Minimum server version: 5.10

        :param bot_user_id: Bot user ID.
        :param include_deleted: If deleted bots should be returned.
        :return: Bot retrieval info
        """

        url = f"{self.api_url}/{bot_user_id}"

        self.reset()
        self.add_application_json_header()
        if include_deleted is not None:
            self.add_to_json('include_deleted', include_deleted)

        return self.request(url, request_type='GET', body=True)

    def disable_bot(self, bot_user_id: str) -> dict:

        """
        Disable a bot.

        Must have manage_bots permission.

        Minimum server version: 5.10

        :param bot_user_id: Bot user ID.
        :return: Bot disable info
        """

        url = f"{self.api_url}/{bot_user_id}/disable"

        self.reset()

        return self.request(url, request_type='POST')

    def enable_bot(self, bot_user_id: str) -> dict:

        """
        Enable a bot.

        Must have manage_bots permission.

        Minimum server version: 5.10

        :param bot_user_id: Bot user ID.
        :return: Bot enable info
        """

        url = f"{self.api_url}/{bot_user_id}/enable"

        self.reset()

        return self.request(url, request_type='POST')

    def assign_bot_to_user(self,
                           bot_user_id: str,
                           user_id: str) -> dict:

        """
        Assign a bot to a specified user.

        Must have manage_bots permission.

        Minimum server version: 5.10

        :param bot_user_id: Bot user ID.
        :param user_id: The user ID to assign the bot to.
        :return: Bot enable info
        """

        url = f"{self.api_url}/{bot_user_id}/assign/{user_id}"

        self.reset()

        return self.request(url, request_type='POST')

    def get_bot_lhs_icon(self, bot_user_id: str) -> dict:

        """
        Get a bot's LHS icon image based on bot_user_id string parameter.

        Must be logged in.

        Minimum server version: 5.14

        :param bot_user_id: Bot user ID.
        :return: Bot LHS icon info
        """

        url = f"{self.api_url}/{bot_user_id}/icon"

        self.reset()

        return self.request(url, request_type='GET')

    def set_bot_lhs_icon_image(self,
                               bot_user_id: str,
                               image: str) -> dict:

        """
        Set a bot's LHS icon image based on bot_user_id string parameter.
        Icon image must be SVG format, all other formats are rejected.

        Must have manage_bots permission.

        Minimum server version: 5.14

        :param bot_user_id: Bot user ID.
        :param image: SVG icon image to be uploaded
        :return: SVG icon image info
        """

        url = f"{self.api_url}/{bot_user_id}/icon"

        self.reset()
        self.add_application_json_header()
        self.add_to_json('image', image)

        return self.request(url, request_type='POST')

    def delete_bot_lhs_icon_image(self, bot_user_id: str) -> dict:

        """
        Delete bot's LHS icon image based on bot_user_id string parameter.

        Must have manage_bots permission.

        Minimum server version: 5.14

        :param bot_user_id: Bot user ID.
        :return: Icon image deletion info
        """

        url = f"{self.api_url}/{bot_user_id}/icon"

        self.reset()

        return self.request(url, request_type='DEL')

    def convert_bot_into_user(self,
                              bot_user_id: str,
                              set_system_admin: bool = None,
                              email: str = None,
                              username: str = None,
                              password: str = None,
                              first_name: str = None,
                              last_name: str = None,
                              nickname: str = None,
                              locale: str = None,
                              position: str = None,
                              props: str = None,
                              notify_props: dict = None) -> dict:

        """
        Convert a bot into a user.

        Must have manage_system permission.

        Minimum server version: 5.26

        :param bot_user_id: Bot user ID.
        :param set_system_admin: Default: false. Whether to give the user the system admin role.
        :param email: User's email.
        :param username: User's name.
        :param password: User's password.
        :param first_name: User's first name.
        :param last_name: User's last name.
        :param nickname: User's nickname.
        :param locale: User's locale.
        :param position: User's position.
        :param props: User's props.
        :param notify_props: User's notify_props.
        :return: Bot conversion info.
        """

        url = f"{self.api_url}/{bot_user_id}/convert_to_user"

        self.reset()
        self.add_application_json_header()
        if set_system_admin is not None:
            self.add_to_json('set_system_admin', set_system_admin)
        if email is not None:
            self.add_to_json('email', email)
        if username is not None:
            self.add_to_json('username', username)
        if password is not None:
            self.add_to_json('password', password)
        if first_name is not None:
            self.add_to_json('first_name', first_name)
        if last_name is not None:
            self.add_to_json('last_name', last_name)
        if nickname is not None:
            self.add_to_json('nickname', nickname)
        if locale is not None:
            self.add_to_json('locale', locale)
        if position is not None:
            self.add_to_json('position', position)
        if props is not None:
            self.add_to_json('props', props)
        if notify_props is not None:
            self.add_to_json('notify_props', notify_props)

        return self.request(url, request_type='POST', body=True)
