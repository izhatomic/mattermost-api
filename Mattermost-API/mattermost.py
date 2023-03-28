from mm_uploads_api import Uploads


class MattermostAPI:
    def __init__(self, token: str, server_url: str):
        self.token = token
        self.server_url = server_url

    @property
    def uploads(self):
        return Uploads(token=self.token, server_url=self.server_url)



