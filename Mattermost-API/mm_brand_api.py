from typing import Union, List, Dict
from Mattermost_Base import Base


class Brand(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/brand"

    def get_brand_image(self) -> dict:
        """
        Get the previously uploaded brand image.
        Returns 404 if no brand image has been uploaded.

        No permission required.

        :return: Brand image retrieval info.
        """
        url = f"{self.api_url}/image"
        self.reset()

        return self.request(url, request_type='GET')

    def upload_brand_image(self, image: str) -> dict:
        """
        Uploads a brand image.

        Must have manage_system permission.

        :param image: The image to be uploaded.
        :return: Brand image upload info.
        """
        url = f"{self.api_url}/image"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('image', image)

        return self.request(url, request_type='POST', body=True)

    def delete_current_brand_image(self) -> dict:
        """
        Deletes the previously uploaded brand image.
        Returns 404 if no brand image has been uploaded.

        Minimum server version: 5.6
        Must have manage_system permission.

        :return: Brand image deletion info.
        """
        url = f"{self.api_url}/image"
        self.reset()

        return self.request(url, request_type='DEL')
