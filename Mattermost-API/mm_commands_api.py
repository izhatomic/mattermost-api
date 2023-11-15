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
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('team_id', team_id)
        self.add_to_json('method', method)
        self.add_to_json('trigger', trigger)
        self.add_to_json('url', url)

        return self.request(url, request_type='POST', body=True)

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
                                        user_input: str) -> dict:
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
