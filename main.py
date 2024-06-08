from loader import Loader
from google.cloud.bigquery import SchemaField
from schema import TABLE_SCHEMA

import argparse
import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

DATA_PATH = "/home/costa/Documentos/desafio_lima/data"


def main(args):
    loader = Loader(namespace="adrenaline", zone="transient")

    page = args.page
    operation = args.operation

    if page = None:
        raise("O argumento --page não foi fornecido")

    if operation == None:
        operation = "load"

    with open(file=f"{DATA_PATH}/{page}.json") as f:
        data = json.load(f)
        
        if operation == "load":
            loader.write_json_data(json_content=data, table_name="artigos", schema=TABLE_SCHEMA)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--page", "-p", type=str, help="Page to be loaded or extracted."
    )
    parser.add_argument(
        "--operation", "-o", type=str, help="Page to be loaded or extracted."
    )
    args = parser.parse_args()
    
    main(args)
