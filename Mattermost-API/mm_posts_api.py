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
        self.add_to_json('id', id)
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
