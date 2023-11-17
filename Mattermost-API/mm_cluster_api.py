from typing import Union, List, Dict
from Mattermost_Base import Base


class Cluster(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/cluster"

    def get_cluster_status(self) -> dict:
        """
        Get a set of information for each node in the cluster,
        useful for checking the status and health of each node.

        Must have manage_system permission.

        :return: Cluster status retrieval info.
        """
        url = f"{self.api_url}/status"
        self.reset()

        return self.request(url, request_type='GET')
