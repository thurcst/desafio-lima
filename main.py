from loader import Loader
from google.cloud.bigquery import SchemaField
from schema import TABLE_SCHEMA
import json


DATA_PATH = "/home/costa/Documentos/desafio_lima/data"


def main():
    loader = Loader(namespace="adrenaline", zone="transient")

    with open(file=f"{DATA_PATH}/artigos.json") as f:
        data = json.load(f)

    loader.write_json_data(json_content=data, table_name="artigos", schema=TABLE_SCHEMA)


if __name__ == "__main__":
    main()
