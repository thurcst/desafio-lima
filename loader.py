"""Implementation of Loader class, which is responsible for collect data and export to GBQ."""

from google.oauth2 import service_account
from google.cloud import bigquery
from typing import IO, List, Dict

PATH = "/home/costa/Documentos/desafio_lima/credentials.json"


class Loader:
    """Loader class job is load information to bigquery table."""

    def __init__(
        self,
        namespace: str,
        zone: str,
        project: str = "lima-project-425805",
    ) -> None:
        self._credentials = service_account.Credentials.from_service_account_file(
            PATH, scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
        self._client = bigquery.Client(project=project, credentials=self._credentials)
        self._dataset = f"{project}.{namespace}_{zone}"
        self._project = project

    def _get_full_table_name(self, table_name: str) -> str:
        return f"{self._dataset}.{table_name}"

    def write_json_data(
        self,
        json_content: List[dict],
        table_name: str,
        schema: list[bigquery.SchemaField],
    ) -> None:
        """Write data from .csv file into a BQ Table.

        Args:
            csv_file (IO): Content of .csv file
            schema (list[bigquery.SchemaField]): Table schema
        """

        job_cfg = bigquery.LoadJobConfig()
        job_cfg.schema_update_options = [
            bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION,
            bigquery.SchemaUpdateOption.ALLOW_FIELD_RELAXATION,
        ]
        job_cfg.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
        job_cfg.schema = schema
        job_cfg.time_partitioning = bigquery.TimePartitioning()

        full_table_name = self._get_full_table_name(table_name)

        job = self._client.load_table_from_json(
            json_content, destination=full_table_name, job_config=job_cfg
        )

        job.result()
