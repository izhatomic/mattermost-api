from typing import Union, List, Dict
from Mattermost_Base import Base


class Threads(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/users"

    def get_threads_user_is_following(self,
                                      user_id: str,
                                      team_id: str,
                                      since: int,
                                      deleted: bool,
                                      extended: bool,
                                      page: int,
                                      pageSize: int,
                                      totalsOnly: bool,
                                      threadsOnly: bool):
        """
        Get all threads that user is following.

        Minimum server version: 5.29
        Must be logged in as the user or have edit_other_users permission.

        :param user_id: The ID of the user. This can also be "me" which will point to the current user.
        :param team_id: The ID of the team in which the thread is.
        :param since: Since filters the threads based on their LastUpdateAt timestamp.
        :param deleted: Default: false. Deleted will specify that even deleted threads should be returned (For mobile sync).
        :param extended: Default: false. Extended will enrich the response with participant details.
        :param page: Default: 0. Page specifies which part of the results to return, by PageSize.
        :param pageSize: Default: 30. PageSize specifies the size of the returned chunk of results.
        :param totalsOnly: Default: false. Setting this to true will only return the total counts.
        :param threadsOnly: Default: false. Setting this to true will only return threads.
        :return: User's threads retrieval info.
        """

        url = f"{self.api_url}/{user_id}/teams/{team_id}/threads"

        self.reset()
        self.add_application_json_header()
        if since is not None:
            self.add_to_json('since', since)
        if deleted is not None:
            self.add_to_json('deleted', deleted)
        if extended is not None:
            self.add_to_json('extended', extended)
        if page is not None:
            self.add_to_json('page', page)
        if pageSize is not None:
            self.add_to_json('pageSize', pageSize)
        if totalsOnly is not None:
            self.add_to_json('totalsOnly', totalsOnly)
        if threadsOnly is not None:
            self.add_to_json('threadsOnly', threadsOnly)

        return self.request(url, request_type='GET', body=True)
    def get_unread_mention_counts_from_followed_threads(self,
                                                        user_id: str,
                                                        team_id: str) -> dict:
        """
        Get all unread mention counts from followed threads.

        Minimum server version: 5.29
        Must be logged in as the user or have edit_other_users permission.

        :param user_id: The ID of the user. This can also be "me" which will point to the current user.
        :param team_id: The ID of the team in which the thread is.
        :return: Get process info.
        """

        url = f"{self.api_url}/{user_id}/teams/{team_id}/threads/mention_counts"

        self.reset()

        return self.request(url, request_type='GET')


