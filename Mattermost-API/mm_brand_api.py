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
