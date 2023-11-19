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

    def mark_all_threads_that_user_following_as_read(self,
                                                     user_id: str,
                                                     team_id: str) -> dict:
        """
        Mark all threads that user is following as read.

        Minimum server version: 5.29
        Must be logged in as the user or have edit_other_users permission.

        :param user_id: The ID of the user. This can also be "me" which will point to the current user.
        :param team_id: The ID of the team in which the thread is.
        :return: User's threads update info.
        """

        url = f"{self.api_url}/{user_id}/teams/{team_id}/threads/read"

        self.reset()

        return self.request(url, request_type='PUT')

    def mark_thread_that_user_following_read_state_to_the_timestamp(self,
                                                                    user_id: str,
                                                                    team_id: str,
                                                                    thread_id: str,
                                                                    timestamp: str) -> dict:
        """
        Mark a thread that user is following as read.

        Minimum server version: 5.29
        Must be logged in as the user or have edit_other_users permission.

        :param user_id: The ID of the user. This can also be "me" which will point to the current user.
        :param team_id: The ID of the team in which the thread is.
        :param thread_id: The ID of the thread to update.
        :param timestamp: The timestamp to which the thread's "last read" state will be reset.
        :return: User's threads update info.
        """

        url = f"{self.api_url}/{user_id}/teams/{team_id}/threads/{thread_id}/read/{timestamp}"

        self.reset()

        return self.request(url, request_type='PUT')

    def mark_thread_that_user_following_as_read_based_on_post_id(self,
                                                                 user_id: str,
                                                                 team_id: str,
                                                                 thread_id: str,
                                                                 post_id: str) -> dict:
        """
        Mark a thread that user is following as unread.

        Minimum server version: 6.7
        Must have read_channel permission for the channel the thread is in or if the channel is public,
        have the read_public_channels permission for the team.
        Must have edit_other_users permission if the user is not the one marking the thread for himself.

        :param user_id: The ID of the user. This can also be "me" which will point to the current user.
        :param team_id: The ID of the team in which the thread is.
        :param thread_id: The ID of the thread to update.
        :param post_id: The ID of a post belonging to the thread to mark as unread.
        :return: User's thread update info.
        """

        url = f"{self.api_url}/{user_id}/teams/{team_id}/threads/{thread_id}/set_unread/{post_id}"

        self.reset()

        return self.request(url, request_type='POST')

    def start_following_thread(self,
                               user_id: str,
                               team_id: str,
                               thread_id: str) -> dict:
        """
        Start following a thread.

        Minimum server version: 5.29
        Must be logged in as the user or have edit_other_users permission.

        :param user_id: The ID of the user. This can also be "me" which will point to the current user.
        :param team_id: The ID of the team in which the thread is.
        :param thread_id: The ID of the thread to update.
        :return: User's thread update info.
        """

        url = f"{self.api_url}/{user_id}/teams/{team_id}/threads/{thread_id}/following"

        self.reset()

        return self.request(url, request_type='PUT')

    def stop_following_thread(self,
                              user_id: str,
                              team_id: str,
                              thread_id: str) -> dict:
        """
        Stop following a thread.

        Minimum server version: 5.29
        Must be logged in as the user or have edit_other_users permission.

        :param user_id: The ID of the user. This can also be "me" which will point to the current user.
        :param team_id: The ID of the team in which the thread is.
        :param thread_id: The ID of the thread to update.
        :return: User's thread update info.
        """

        url = f"{self.api_url}/{user_id}/teams/{team_id}/threads/{thread_id}/following"

        self.reset()

        return self.request(url, request_type='DEL')

    def get_thread_followed_by_user(self,
                                    user_id: str,
                                    team_id: str,
                                    thread_id: str) -> dict:
        """
        Get a thread.

        Minimum server version: 5.29
        Must be logged in as the user or have edit_other_users permission.

        :param user_id: The ID of the user. This can also be "me" which will point to the current user.
        :param team_id: The ID of the team in which the thread is.
        :param thread_id: The ID of the thread to follow.
        :return: User's thread update info.
        """

        url = f"{self.api_url}/{user_id}/teams/{team_id}/threads/{thread_id}"

        self.reset()

        return self.request(url, request_type='GET')
