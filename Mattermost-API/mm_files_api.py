from typing import Union, List, Dict
from Mattermost_Base import Base


class File(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/files"

    def upload_a_file(self,
                      channel_id: str,
                      filename: str,
                      files: str,
                      client_ids: str) -> dict:
        """
        Uploads a file that can later be attached to a post.

        This request can either be a multipart/form-data request with a channel_id,
        files and optional client_ids defined in the FormData, or it can be a
        request with the channel_id and filename defined as query parameters with
        the contents of a single file in the body of the request.

        Only multipart/form-data requests are supported by server versions up to
        and including 4.7. Server versions 4.8 and higher support both types of
        requests.

        Must have upload_file permission.

        :param channel_id: The ID of the channel that this file will be uploaded to.
        :param filename: The name of the file to be uploaded.
        :param files: A file to be uploaded.
        :param client_ids: A unique identifier for the file that will be returned in the response.
        :return: Corresponding lists and metadata info
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        if channel_id is not None:
            self.add_to_json('channel_id', channel_id)
        if filename is not None:
            self.add_to_json('filename', filename)
        if files is not None:
            self.add_to_json('files', files)
        if client_ids is not None:
            self.add_to_json('client_ids', client_ids)

        return self.request(url, request_type='POST', body=True)

    def get_a_file(self,
                   file_id: str) -> dict:
        """
        Gets a file that has been uploaded previously.

        Must have read_channel permission or be uploader of the file.

        :param file_id: The ID of the channel that this file will be uploaded to.
        :return: Corresponding lists and metadata info
        """
        url = f"{self.api_url}/{file_id}"
        self.reset()

        return self.request(url, request_type='GET')

    def get_file_thumbnail(self,
                           file_id: str) -> dict:
        """
        Gets a file's thumbnail.

        Must have read_channel permission or be uploader of the file.

        :param file_id: The ID of the file to get.
        :return: File's thumbnail info
        """
        url = f"{self.api_url}/{file_id}/thumbnail"
        self.reset()

        return self.request(url, request_type='GET')

    def get_file_preview(self, file_id: str) -> dict:
        """
        Gets a file's preview.

        Must have read_channel permission or be uploader of the file.

        :param file_id: The ID of the file to get.
        :return: File's preview info
        """
        url = f"{self.api_url}/{file_id}/preview"
        self.reset()

        return self.request(url, request_type='GET')

    def get_public_file_link(self, file_id: str) -> dict:
        """
        Gets a public link for a file that can be accessed without logging into Mattermost.

        Must have read_channel permission or be uploader of the file.

        :param file_id: The ID of the file to get a link for.
        :return: Public file link info
        """
        url = f"{self.api_url}/{file_id}/link"
        self.reset()

        return self.request(url, request_type='GET')

    def get_metadata_for_file(self, file_id: str) -> dict:
        """
        Gets a file's info.

        Must have read_channel permission or be uploader of the file.

        :param file_id: The ID of the file info to get.
        :return: Stored metadata info.
        """
        url = f"{self.api_url}/{file_id}/info"
        self.reset()

        return self.request(url, request_type='GET')

    def get_public_file(self,
                        file_id: str,
                        h: str) -> dict:
        """
        Gets a public file.

        No permissions required.

        :param file_id: The ID of the file to get.
        :param h: File hash.
        :return: Public file info.
        """
        url = f"{self.api_url}/{file_id}/public"
        self.reset()
        self.add_application_json_header()
        if h is not None:
            self.add_to_json('h', h)

        return self.request(url, request_type='GET')

    def search_files_in_team(self,
                             team_id: str,
                             terms: str,
                             is_or_search: bool,
                             time_zone_offset: int,
                             include_deleted_channels: bool,
                             page: int,
                             per_page: int) -> dict:
        """
        Search for files in a team based on file name, extention and file content
        (if file content extraction is enabled and supported for the files).

        Must be authenticated and have the view_team permission.

        Minimum server version: 5.34

        :param team_id: Team GUID.
        :param terms: The search terms as inputed by the user. To search for files from a user
        include from:someusername, using a user's username. To search in a specific channel
        include in:somechannel, using the channel name (not the display name).
        To search for specific extensions included ext:extension.
        :param is_or_search: Set to true if an Or search should be performed vs an And search.
        :param time_zone_offset: Default: 0. Offset from UTC of user timezone for date searches.
        :param include_deleted_channels: Set to true if deleted channels should be included in the search. (archived channels)
        :param page: Default: 0. The page to select. (Only works with Elasticsearch)
        :param per_page: Default: 60. The number of posts per page. (Only works with Elasticsearch)
        :return: Files list retrieval info.
        """
        url = f"{self.base_url}/teams/{team_id}/files/search"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('terms', terms)
        self.add_to_json('is_or_search', is_or_search)
        if time_zone_offset is not None:
            self.add_to_json('time_zone_offset', time_zone_offset)
        if include_deleted_channels is not None:
            self.add_to_json('include_deleted_channels', include_deleted_channels)
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)
