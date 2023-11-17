from typing import Union, List, Dict
from Mattermost_Base import Base


class Jobs(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/jobs"

    def get_the_jobs(self,
                     page: int,
                     per_page: int) -> dict:
        """
        Get a page of jobs. Use the query parameters to
        modify the behaviour of this endpoint.

        Minimum server version: 4.1
        Must have manage_jobs permission.

        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of jobs per page.
        :return: Jobs list retrieval info.
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)

    def create_a_new_job(self,
                         type: str,
                         data: dict) -> dict:
        """
        Create a new job

        Minimum server version: 4.1
        Must have manage_jobs permission.

        :param type: The type of job to create.
        :param data: An object containing any additional data required for this job type.
        :return: Job creation info.
        """
        url = f"{self.api_url}/"
        self.reset()
        self.add_application_json_header()
        self.add_to_json('type', type)
        if data is not None:
            self.add_to_json('data', data)

        return self.request(url, request_type='POST', body=True)

    def get_a_job(self, job_id: str) -> dict:
        """
        Gets a single job.

        Minimum server version: 4.1
        Must have manage_jobs permission.

        :param job_id: The type of job to create.
        :return: Job retrieval info.
        """
        url = f"{self.api_url}/{job_id}"
        self.reset()

        return self.request(url, request_type='GET')

    def download_the_results_of_job(self, job_id: str) -> dict:
        """
        Download the result of a single job.

        Minimum server version: 5.28
        Must have manage_jobs permission.

        :param job_id: Job GUID.
        :return: Results status.
        """
        url = f"{self.api_url}/{job_id}/download"
        self.reset()

        return self.request(url, request_type='GET')

    def cancel_a_job(self, job_id: str) -> dict:
        """
        Cancel a job.

        Minimum server version: 4.1
        Must have manage_jobs permission.

        :param job_id: Job GUID.
        :return: Job cancellation info.
        """
        url = f"{self.api_url}/{job_id}/download"
        self.reset()

        return self.request(url, request_type='POST')

    def get_jobs_of_given_type(self,
                               type: str,
                               page: int,
                               per_page: int) -> dict:
        """
        Get a page of jobs of the given type.
        Use the query parameters to modify the behaviour of this endpoint.

        Minimum server version: 4.1
        Must have manage_jobs permission.

        :param type: Job type.
        :param page: Default: 0. The page to select.
        :param per_page: Default: 60. The number of jobs per page.
        :return: Job list status.
        """
        url = f"{self.api_url}/type/{type}"
        self.reset()
        self.add_application_json_header()
        if page is not None:
            self.add_to_json('page', page)
        if per_page is not None:
            self.add_to_json('per_page', per_page)

        return self.request(url, request_type='GET', body=True)
