from fastapi import FastAPI
from reader import Reader

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/artigos")
async def artigos():
    reader = Reader()

    query = """
    SELECT *
    FROM `adrenaline_transient.artigos`
    """

    data = reader.query_from_bq(query)

    return data


@app.get("/artigos/keywords")
async def artigos_by_keyword(keywords: str | None = None):
    reader = Reader()

    query = """
    SELECT *
    FROM `adrenaline_transient.artigos`
    """

    if keywords:
        filter_params = f"""
        WHERE '{keywords}' IN UNNEST(tags)
        """

        query = query + filter_params

        logger.debug(query)

    data = reader.query_from_bq(query)

    return data
