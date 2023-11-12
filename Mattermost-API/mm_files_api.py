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
