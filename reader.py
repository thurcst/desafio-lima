from google.cloud.bigquery import Client
from google.oauth2 import service_account
from typing import List

PATH = "/home/costa/Documentos/desafio_lima/credentials.json"


class Reader:
    def __init__(
        self,
        project: str = "lima-project-425805",
    ) -> None:
        self._credentials = service_account.Credentials.from_service_account_file(
            PATH, scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
        self.client = Client(project, credentials=self._credentials)

    def query_from_bq(self, query: str) -> List[dict]:
        job = self.client.query(query)
        query_results = job.result()

        data = [dict(row) for row in query_results]

        return data
