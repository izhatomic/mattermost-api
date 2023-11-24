from typing import Union, List, Dict
from Mattermost_Base import Base


class Posts(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/posts"

    def create_post(self,
                    set_online: bool,
                    channel_id: str,
                    message: str = None,
                    root_id: str = None,
                    file_ids: list[str] = None,
                    props: dict = None,
                    metadata: dict = None) -> dict:
        """
        Create a new post in a channel. To create the post as a comment on another post,
        provide root_id.

        Must have create_post permission for the channel the post is being created in.

        :param set_online: Whether to set the user status as online or not.
        :param channel_id: The channel ID to post in.
        :param message: The message contents, can be formatted with Markdown.
        :param root_id: The post ID to comment on.
        :param file_ids: A list of file IDs to associate with the post.
        Note that posts are limited to 5 files maximum. Please use additional posts for more files.
        :param props: A general JSON property bag to attach to the post
        :param metadata: A JSON object to add post metadata, e.g the post's priority
        :return: Post creation info.
        """

        url = f"{self.api_url}"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('set_online', set_online)
        self.add_to_json('channel_id', channel_id)
        if message is not None:
            self.add_to_json('message', message)
        if root_id is not None:
            self.add_to_json('root_id', root_id)
        if file_ids is not None:
            self.add_to_json('file_ids', file_ids)
        if props is not None:
            self.add_to_json('props', props)
        if metadata is not None:
            self.add_to_json('metadata', metadata)

        return self.request(url, request_type='POST', body=True)

    def create_ephemeral_post(self,
                              user_id: str,
                              post: dict) -> dict:
        """
        Create a new ephemeral post in a channel.

        Must have create_post_ephemeral permission (currently only given to system admin)

        :param user_id: The target user id for the ephemeral post.
        :param post: Post object to create.
        :return: Post creation info.
        """

        url = f"{self.api_url}/ephemeral"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('user_id', user_id)
        self.add_to_json('post', post)

        return self.request(url, request_type='POST', body=True)

    def get_post(self,
                 post_id: str,
                 include_deleted: bool) -> dict:
        """
        Get a single post.

        Must have read_channel permission for the channel the post is in or if the channel is public,
        have the read_public_channels permission for the team.

        :param post_id: ID of the post to get.
        :param include_deleted: Default: false. Defines if result should
        include deleted posts, must have 'manage_system' (admin) permission.
        :return: Post retrieval info.
        """

        url = f"{self.api_url}/{post_id}"
        self.reset()
        self.add_application_json_header()
        if include_deleted is not None:
            self.add_to_json('include_deleted', include_deleted)

        return self.request(url, request_type='GET', body=True)

    def delete_post(self, post_id: str) -> dict:
        """
        Soft deletes a post, by marking the post as deleted in the database.
        Soft deleted posts will not be returned in post queries.

        Must be logged in as the user or have delete_others_posts permission.

        :param post_id: ID of the post to delete.
        :return: Post deletion info.
        """

        url = f"{self.api_url}/{post_id}"
        self.reset()

        return self.request(url, request_type='DEL')

    def update_post(self,
                    post_id: str,
                    id: str,
                    is_pinned: bool = None,
                    message: str = None,
                    has_reactions: bool = None,
                    props: str = None) -> dict:
        """
        Update a post. Only the fields listed below are updatable,
        omitted fields will be treated as blank.

        Must have edit_post permission for the channel the post is in.

        :param post_id: ID of the post to update.
        :param id: ID of the post to update.
        :param is_pinned: The size of the file to upload in bytes.
        :param message: The message text of the post.
        :param has_reactions: Set to true if the post has reactions to it.
        :param props: A general JSON property bag to attach to the post
        :return: Post update info.
        """

        url = f"{self.api_url}/{post_id}"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('id', id)
        if is_pinned is not None:
            self.add_to_json('is_pinned', is_pinned)
        if message is not None:
            self.add_to_json('message', message)
        if has_reactions is not None:
            self.add_to_json('has_reactions', has_reactions)
        if props is not None:
            self.add_to_json('props', props)

        return self.request(url, request_type='PUT', body=True)

    def mark_as_unread_from_post(self,
                                 user_id: str,
                                 post_id: str) -> dict:
        """
        Mark a channel as being unread from a given post.

        Must have read_channel permission for the channel the post is in or if the channel is public,
        have the read_public_channels permission for the team. Must have edit_other_users permission
        if the user is not the one marking the post for himself.

        :param user_id: User GUID.
        :param post_id: Post GUID.
        :return: Post info.
        """

        url = f"{self.base_url}/users/{user_id}/post/{post_id}/set_unread"
        self.reset()

        return self.request(url, request_type='POST')

    def patch_post(self,
                   post_id:str,
                   is_pinned:bool,
                   message:str,
                   file_ids:list[str],
                   has_reactions:bool,
                   props:str)->dict:
        """
        Partially update a post by providing only the fields you want to update.
        Omitted fields will not be updated. The fields that can be updated are defined in the request body,
        all other provided fields will be ignored.

        Must have the edit_post permission.

        :param post_id: Post GUID.
        :param is_pinned: Set to true to pin the post to the channel it is in.
        :param message: The message text of the post.
        :param file_ids: The list of files attached to this post.
        :param has_reactions: Set to true if the post has reactions to it.
        :param props: A general JSON property bag to attach to the post.
        :return: Post patch info.
        """

        url = f"{self.api_url}/{post_id}/patch"
        self.reset()
        self.add_application_json_header()
        if is_pinned is not None:
            self.add_to_json('is_pinned', is_pinned)
        if message is not None:
            self.add_to_json('message', message)
        if file_ids is not None:
            self.add_to_json('file_ids', file_ids)
        if has_reactions is not None:
            self.add_to_json('has_reactions', has_reactions)
        if props is not None:
            self.add_to_json('props', props)

        return self.request(url, request_type='PUT', body=True)

    def get_thread(self,
                   post_id: str,
                   perPage: int = None,
                   fromPost: str = None,
                   fromCreateAt: int = None,
                   direction: str = None,
                   skipFetchThreads: bool = None,
                   collapsedThreads: bool = None,
                   collapsedThreadsExtended: bool = None) -> dict:
        """
        Get a post and the rest of the posts in the same thread.

        Must have read_channel permission for the channel
        the post is in or if the channel is public, have the read_public_channels permission for the team.

        :param post_id: ID of a post in the thread.
        :param perPage: Default: 0. The number of posts per page.
        :param fromPost: Default: "". The post_id to return the next page of posts from.
        :param fromCreateAt: Default: 0. The create_at timestamp to return the next page of posts from.
        :param direction: Default: "". The direction to return the posts. Either up or down.
        :param skipFetchThreads: Default: false. Whether to skip fetching threads or not.
        :param collapsedThreads: Default: false. Whether the client uses CRT or not
        :param collapsedThreadsExtended: Default: false. Whether to return the associated users as part of the response or not
        :return: Post list retrieval info.
        """

        url = f"{self.api_url}/{post_id}/thread"
        self.reset()
        self.add_application_json_header()
        if perPage is not None:
            self.add_to_json('perPage', perPage)
        if fromPost is not None:
            self.add_to_json('fromPost', fromPost)
        if fromCreateAt is not None:
            self.add_to_json('fromCreateAt', fromCreateAt)
        if direction is not None:
            self.add_to_json('direction', direction)
        if skipFetchThreads is not None:
            self.add_to_json('skipFetchThreads', skipFetchThreads)
        if collapsedThreads is not None:
            self.add_to_json('collapsedThreads', collapsedThreads)
        if collapsedThreadsExtended is not None:
            self.add_to_json('collapsedThreadsExtended', collapsedThreadsExtended)

        return self.request(url, request_type='GET', body=True)

    def get_list_of_flagged_posts(self,
                                  user_id: str,
                                  team_id: str = None,
                                  channel_id: str = None,
                                  page: int = None,
                                  per_page: int = None) -> dict:
        """
        Get a page of flagged posts of a user provided user id string. Selects from a channel, team,
        or all flagged posts by a user. Will only return posts from channels in which the user is member.

        Must be user or have manage_system permission.

        :param user_id: ID of the user
        :param team_id: Team ID
        :param channel_id: Channel ID
        :param page: Default: 0. The page to select
        :param per_page: Default: 60. The number of posts per page
        :return: Post list retrieval info
        """

        url = f"{self.base_url}/users/{user_id}/posts/flagged"

        self.reset()
        self.add_application_json_header()
        if team_id is not None:
            self.add_to_json('team_id', team_id)
        if channel_id is not None:
            self.add_to_json('channel_id', channel_id)
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)

    def get_file_info_for_post(self, post_id: str) -> dict:
        """
        Gets a list of file information objects for the files attached to a post.

        Must have read_channel permission for the channel the post is in.

        :param post_id: ID of the post
        :return: File info retrieval info
        """

        url = f"{self.api_url}/{post_id}/files/info"

        self.reset()

        return self.request(url, request_type='GET')

    def get_posts_for_channel(self,
                              channel_id: str,
                              page: int = None,
                              per_page: int = None,
                              since: int = None,
                              before: str = None,
                              after: str = None,
                              include_deleted: bool = None) -> dict:
        """
        Get a page of posts in a channel. Use the query parameters to modify the behaviour of this endpoint.
        The parameter since must not be used with any of before, after, page, and per_page parameters.
        If since is used, it will always return all posts modified since that time, ordered by their create time
        limited till 1000. A caveat with this parameter is that there is no guarantee that the returned posts will
        be consecutive. It is left to the clients to maintain state and fill any missing holes in the post order.

        Must have read_channel permission for the channel.

        :param channel_id: The channel ID to get the posts for
        :param page: Default: 0. The page to select
        :param per_page: Default: 60. The number of posts per page
        :param since: Provide a non-zero value in Unix time milliseconds to select posts modified after that time
        :param before: A post id to select the posts that came before this one
        :param after: A post id to select the posts that came after this one
        :param include_deleted: ID of the post
        :return: Post list retrieval info
        """

        url = f"{self.base_url}/channnels/{channel_id}/posts"

        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)
        if since is not None:
            self.add_to_json('since', since)
        if before is not None:
            self.add_to_json('before', before)
        if after is not None:
            self.add_to_json('after', after)
        if include_deleted is not None:
            self.add_to_json('include_deleted', include_deleted)

        return self.request(url, request_type='GET', body=True)

    def get_posts_around_oldest_unread(self,
                                       user_id: str,
                                       channel_id: str,
                                       limit_before: int = None,
                                       limit_after: int = None,
                                       skipFetchThreads: bool = None,
                                       collapsedThreads: bool = None,
                                       collapsedThreadsExtended: bool = None) -> dict:
        """
        Get the oldest unread post in the channel for the given user as well as the posts around it.
        The returned list is sorted in descending order (most recent post first).

        Must be logged in as the user or have edit_other_users permission,
        and must have read_channel permission for the channel.

        Minimum server version: 5.14

        :param user_id: ID of the user
        :param channel_id: The channel ID to get the posts for
        :param limit_before: Default: 60. Number of posts before the oldest unread posts.
        Maximum is 200 posts if limit is set greater than that.
        :param limit_after: Default: 60. Number of posts after and including the oldest unread post.
        Maximum is 200 posts if limit is set greater than that.
        :param skipFetchThreads: Default: false. Whether to skip fetching threads or not
        :param collapsedThreads: Default: false. Whether the client uses CRT or not
        :param collapsedThreadsExtended: Default: false. Whether to return the associated
        users as part of the response or not
        :return: Post list retrieval info
        """

        url = f"{self.base_url}/users/{user_id}/channels/{channel_id}/posts/unread"

        self.reset()
        self.add_application_json_header()
        if limit_before is not None:
            self.add_to_json('limit_before', limit_before)
        if limit_after is not None:
            self.add_to_json('limit_after', limit_after)
        if skipFetchThreads is not None:
            self.add_to_json('skipFetchThreads', skipFetchThreads)
        if collapsedThreads is not None:
            self.add_to_json('collapsedThreads', collapsedThreads)
        if collapsedThreadsExtended is not None:
            self.add_to_json('collapsedThreadsExtended', collapsedThreadsExtended)

        return self.request(url, request_type='GET', body=True)

    def search_for_team_posts(self,
                              team_id:str,
                              terms:str,
                              is_or_search:bool,
                              time_zone_offset:int=None,
                              include_deleted_channels:bool=None,
                              page:int=None,
                              per_page:int=None)->dict:
        """
        Search posts in the team and from the provided terms string.

        Must be authenticated and have the view_team permission.

        Minimum server version: 5.14

        :param user_id: Team GUID
        :param terms: The search terms as inputed by the user. To search for posts from a user include
        from:someusername, using a user's username. To search in a specific channel include in:somechannel,
        using the channel name (not the display name).
        :param is_or_search: Set to true if an Or search should be performed vs an And search.
        :param time_zone_offset: Default: 0. Offset from UTC of user timezone for date searches.
        :param include_deleted_channels: Set to true if deleted channels should be
        included in the search. (archived channels)
        :param page: Default: 0. The page to select. (Only works with Elasticsearch)
        :param per_page: Default: Default: 60. The number of posts per page. (Only works with Elasticsearch)
        :return: Post list retrieval info
        """

        url = f"{self.base_url}/teams/{team_id}/posts/search"

        self.reset()
        self.add_application_json_header()
        if terms is not None:
            self.add_to_json('terms', terms)
        if is_or_search is not None:
            self.add_to_json('is_or_search', is_or_search)
        if time_zone_offset is not None:
            self.add_to_json('time_zone_offset', time_zone_offset)
        if include_deleted_channels is not None:
            self.add_to_json('include_deleted_channels', include_deleted_channels)
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='POST', body=True)

