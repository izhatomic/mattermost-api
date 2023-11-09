from typing import Union, List, Dict
from Mattermost_Base import Base


class Reactions(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/reactions"

    def create_a_reaction(self,
                          user_id: str,
                          post_id: str,
                          emoji_name: str,
                          create_at: int) -> dict:
        """
        Create a reaction.

        Must have read_channel permission for the channel the post is in.

        :param user_id: The ID of the user that made this reaction.
        :param post_id: The ID of the post to which this reaction was made.
        :param emoji_name: The name of the emoji that was used for this reaction.
        :param create_at: The time in milliseconds this reaction was made.
        :return: Reaction creation info.
        """

        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        if user_id is not None:
            self.add_to_json('user_id', user_id)
        if post_id is not None:
            self.add_to_json('post_id', post_id)
        if emoji_name is not None:
            self.add_to_json('emoji_name', emoji_name)
        if create_at is not None:
            self.add_to_json('create_at', create_at)

        return self.request(url, request_type='POST', body=True)

    def get_list_of_reactions_to_post(self, post_id: str) -> dict:
        """
        Get a list of reactions made by all users to a given post.

        Must have read_channel permission for the channel the post is in.

        :param post_id: ID of a post.
        :return: Reaction list retrieval info.
        """

        url = f"{self.base_url}/posts/{post_id}/reactions"
        self.reset()

        return self.request(url, request_type='GET')
