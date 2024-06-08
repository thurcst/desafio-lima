from fastapi import FastAPI, Response
from reader import Reader

import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/noticias")
async def noticias():
    logger.info("Starting collect proccess from noticias table.")
    reader = Reader()

    query = """
    SELECT *
    FROM `adrenaline_transient.noticias`
    """

    try:
        data = reader.query_from_bq(query)
        status = 200

    except Exception as e:
        data = "Error while extracting data. {}".format(e)
        status = 400

    data = json.dumps(data)

    return Response(content=data, status_code=status)


@app.get("/analises")
async def analises():
    logger.info("Starting collect proccess from analises table.")
    reader = Reader()

    query = """
    SELECT *
    FROM `adrenaline_transient.analises`
    """
    try:
        data = reader.query_from_bq(query)
        status = 200

    except Exception as e:
        data = "Error while extracting data. {}".format(e)
        status = 400

    data = json.dumps(data)

    return Response(content=data, status_code=status)


@app.get("/artigos")
async def artigos():
    logger.info("Starting collect proccess from artigos table.")
    reader = Reader()

    query = """
    SELECT *
    FROM `adrenaline_transient.artigos`
    """
    try:
        data = reader.query_from_bq(query)
        status = 200

    except Exception as e:
        data = "Error while extracting data. {}".format(e)
        status = 400

    data = json.dumps(data)

    return Response(content=data, status_code=status)


@app.get("/artigos/keywords")
async def artigos_by_keyword(keywords: str):
    reader = Reader()

    query = f"""
    SELECT *
    FROM `adrenaline_transient.artigos`
    WHERE '{keywords}' IN UNNEST(tags)
    """
    try:
        data = reader.query_from_bq(query)
        status = 200

    except Exception as e:
        data = "Error while extracting data. {}".format(e)
        status = 400

    data = json.dumps(data)

    return Response(content=data, status_code=status)


@app.get("/noticias/keywords")
async def noticias_by_keyword(keywords: str):
    reader = Reader()

    query = f"""
    SELECT *
    FROM `adrenaline_transient.noticias`
    WHERE '{keywords}' IN UNNEST(tags)
    """
    try:
        data = reader.query_from_bq(query)
        status = 200

    except Exception as e:
        data = "Error while extracting data. {}".format(e)
        status = 400

    data = json.dumps(data)

    return Response(content=data, status_code=status)


@app.get("/analises/keywords")
async def analises_by_keyword(keywords: str):
    reader = Reader()

    query = f"""
    SELECT *
    FROM `adrenaline_transient.analises`
    WHERE '{keywords}' IN UNNEST(tags)
    """
    try:
        data = reader.query_from_bq(query)
        status = 200

    except Exception as e:
        data = "Error while extracting data. {}".format(e)
        status = 400

    data = json.dumps(data)

    return Response(content=data, status_code=status)
