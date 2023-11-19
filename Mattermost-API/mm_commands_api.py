from typing import Union, List, Dict
from Mattermost_Base import Base


class Commands(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/commands"

    def create_a_command(self,
                         team_id: str,
                         method: str,
                         trigger: str,
                         url: str) -> dict:
        """
        Create a command for a team.
        manage_slash_commands for the team the command is in.

        :param team_id: Team ID to where the command should be created.
        :param method: 'P' for post request, 'G' for get request.
        :param trigger: Activation word to trigger the command.
        :param url: The URL that the command will make the request.
        :return: Command creation info.
        """
        api_url = f"{self.api_url}/"
        self.reset()
                             
        self.add_application_json_header()
        self.add_to_json('team_id', team_id)
        self.add_to_json('method', method)
        self.add_to_json('trigger', trigger)
        self.add_to_json('url', url)

        return self.request(api_url, request_type='POST', body=True)

    def list_commands_for_team(self,
                               team_id: str,
                               custom_only: bool) -> dict:
        """
        List commands for a team.
        manage_slash_commands if need list custom commands.
        :param team_id: The team id.
        :param custom_only: Default: false. To get only the custom commands. If set to false will get the custom if the user have access plus the system commands, otherwise just the system commands.
        :return: List commands retrieval info.
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('team_id', team_id)
        self.add_to_json('custom_only', custom_only)

        return self.request(url, request_type='GET', body=True)

    def list_autocomplete_commands(self, team_id: str) -> dict:
        """
        List autocomplete commands in the team.
        view_team for the team.
        :param team_id: Team GUID.
        :return: Autocomplete commands retrieval info.
        """
        url = f"{self.base_url}/teams/{team_id}/commands/autocomplete"
        self.reset()

        return self.request(url, request_type='GET')

    def list_commands_autocomplete_data(self,
                                        team_id: str,
                                        user_input: str = None) -> dict:
        """
        List commands' autocomplete data for the team.
        Minimum server version: 5.24
        view_team for the team.
        :param team_id: Team GUID.
        :param user_input: String inputted by the user.
        :return: Commands' autocomplete data retrieval info.
        """
        url = f"{self.base_url}/teams/{team_id}/commands/autocomplete_suggestions"
        self.reset()
        self.add_application_json_header()
        if user_input is not None:
            self.add_to_json('user_input', user_input)

        return self.request(url, request_type='GET', body=True)

    def get_a_command(self, command_id: str) -> dict:
        """
        Get a command definition based on command id string.
        Minimum server version: 5.22
        Must have manage_slash_commands permission for the team the command is in.
        :param command_id: ID of the command to get.
        :return: Command get info.
        """
        url = f"{self.api_url}/{command_id}"
        self.reset()

        return self.request(url, request_type='GET')

    def update_a_command(self,
                         command_id: str,
                         id: str = None,
                         token: str = None,
                         create_at: int = None,
                         update_at: int = None,
                         delete_at: int = None,
                         creator_id: str = None,
                         team_id: str = None,
                         trigger: str = None,
                         method: str = None,
                         username: str = None,
                         icon_url: str = None,
                         auto_complete: bool = None,
                         auto_complete_desc: str = None,
                         auto_complete_hint: str = None,
                         display_name: str = None,
                         description: str = None,
                         url: str = None) -> dict:
        """
        Update a single command based on command id string and Command struct.
        Must have manage_slash_commands permission for the team the command is in.
        :param command_id: ID of the command to update
        :param id: The ID of the slash command.
        :param token: The token which is used to verify the source of the payload.
        :param create_at: The time in milliseconds the command was created.
        :param update_at: The time in milliseconds the command was last updated.
        :param delete_at: The time in milliseconds the command was deleted, 0 if never deleted
        :param creator_id: The user id for the commands creator
        :param team_id: The team id for which this command is configured
        :param trigger: The string that triggers this command
        :param method: Is the trigger done with HTTP Get ('G') or HTTP Post ('P')
        :param username: What is the username for the response post
        :param icon_url: The url to find the icon for this users avatar
        :param auto_complete: Use auto complete for this command
        :param auto_complete_desc: The description for this command shown when selecting the command
        :param auto_complete_hint: The hint for this command
        :param display_name: Display name for the command
        :param description: Description for this command
        :param url: The URL that is triggered
        :return: Command update info.
        """
        api_url = f"{self.api_url}/{command_id}"
        self.reset()
        self.add_application_json_header()
                             
        if id is not None:
            self.add_to_json('id', id)
        if token is not None:
            self.add_to_json('token', token)
        if create_at is not None:
            self.add_to_json('create_at', create_at)
        if update_at is not None:
            self.add_to_json('update_at', update_at)
        if delete_at is not None:
            self.add_to_json('delete_at', delete_at)
        if creator_id is not None:
            self.add_to_json('creator_id', creator_id)
        if team_id is not None:
            self.add_to_json('team_id', team_id)
        if trigger is not None:
            self.add_to_json('trigger', trigger)
        if method is not None:
            self.add_to_json('method', method)
        if username is not None:
            self.add_to_json('username', username)
        if icon_url is not None:
            self.add_to_json('icon_url', icon_url)
        if auto_complete is not None:
            self.add_to_json('auto_complete', auto_complete)
        if auto_complete_desc is not None:
            self.add_to_json('auto_complete_desc', auto_complete_desc)
        if auto_complete_hint is not None:
            self.add_to_json('auto_complete_hint', auto_complete_hint)
        if display_name is not None:
            self.add_to_json('display_name', display_name)
        if description is not None:
            self.add_to_json('description', description)
        if url is not None:
            self.add_to_json('url', url)

        return self.request(api_url, request_type='PUT', body=True)

    def delete_a_command(self, command_id: str) -> dict:
        """
        Delete a command based on command id string.
        Must have manage_slash_commands permission for the team the command is in.
        :param command_id: ID of the command to delete.
        :return: Command deletion info.
        """
        url = f"{self.api_url}/{command_id}"
        self.reset()

        return self.request(url, request_type='DEL')

    def move_a_command(self,
                       command_id: str,
                       team_id: str = None) -> dict:
        """
        Move a command to a different team based on command id string.
        Must have manage_slash_commands permission for the team the command is in.
        :param command_id: ID of the command to move.
        :param team_id: Destination teamId
        :return: Command move info.
        """
        url = f"{self.api_url}/{command_id}/move"
        self.reset()
        self.add_application_json_header()
        if team_id is not None:
            self.add_to_json('team_id', team_id)

        return self.request(url, request_type='PUT', body=True)

    def generate_new_token(self, command_id: str) -> dict:
        """
        Generate a new token for the command based on command id string.
        Must have manage_slash_commands permission for the team the command is in.
        :param command_id: ID of the command to generate the new token.
        :return: Token generation info.
        """
        url = f"{self.api_url}/{command_id}/regen_token"
        self.reset()

        return self.request(url, request_type='PUT')

    def execute_a_command(self,
                          channel_id: str,
                          command: str) -> dict:
        """
        Execute a command on a team.
        Must have manage_slash_commands permission for the team the command is in.
        :param channel_id: Channel Id where the command will execute
        :param command: The slash command to execute, including parameters. Eg, '/echo bounces around the room'
        :return: Command execution info.
        """
        url = f"{self.api_url}/execute"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('channel_id', channel_id)
        self.add_to_json('command', command)

        return self.request(url, request_type='POST', body=True)
