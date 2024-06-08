from google.oauth2 import service_account
from scrapy.exceptions import DropItem
from google.cloud import bigquery
from adrenaline.schema import TABLE_SCHEMA

import logging
import json


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
logger = logging.getLogger()

PATH = "/home/costa/Documentos/desafio_lima/credentials.json"


class BigqueryPipeline:

    def __init__(self, project_id: str, dataset_id: str, table_id: str) -> None:
        self.project_id = project_id
        self._dataset = dataset_id
        self.table_id = table_id
        self.dataset_ref = bigquery.DatasetReference(
            project=self.project_id, dataset_id=self._dataset
        )

        self._credentials = service_account.Credentials.from_service_account_file(
            PATH, scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
        self._client = bigquery.Client(
            project=self.project_id, credentials=self._credentials
        )

    @classmethod
    def from_crawler(cls, crawler):
        project_id = crawler.settings.get("BIGQUERY_PROJECT_ID")
        dataset_id = crawler.settings.get("BIGQUERY_DATASET_ID")
        table_id = crawler.spider.name
        return cls(project_id, dataset_id, table_id)

    def process_item(self, item, spider):
        try:

            job_cfg = bigquery.LoadJobConfig()
            job_cfg.schema_update_options = [
                bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION,
                bigquery.SchemaUpdateOption.ALLOW_FIELD_RELAXATION,
            ]
            job_cfg.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
            job_cfg.schema = TABLE_SCHEMA
            job_cfg.time_partitioning = bigquery.TimePartitioning()

            full_table_name = self._get_full_table_name(self.table_id)

            table_ref = self._client.dataset(self._dataset).table(self.table_id)

            if not self.exists(full_table_name):
                table = self._create_table()
            else:
                table = self._client.get_table(table_ref)

            errors = self._client.insert_rows_json(table, [dict(item)])

            if errors:
                logger.error(f"Erro ao carregar item no BigQuery: {errors}")
            else:
                logger.info("Item carregado com sucesso no BigQuery")

            return item
        except Exception as e:
            raise DropItem(f"Error processing item: {e}")

    def _get_full_table_name(self, table_name: str) -> str:
        return f"{self._dataset}.{table_name}"

    def _create_table(self):
        schema = TABLE_SCHEMA

        table_ref = self._client.dataset(self._dataset).table(self.table_id)
        table = bigquery.Table(table_ref, schema=schema)

        result = self._client.create_table(table)

        return result

    def exists(self, full_name: str) -> bool:
        try:
            self._client.get_table(full_name)
            return True
        except Exception:
            return False
