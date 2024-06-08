from adrenaline.adrenaline.spiders import artigos, analises, noticias
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

import argparse
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

DATA_PATH = "/home/costa/Documentos/desafio_lima/data"


def main(args):
    """Receive the page and the operation from args and run spider to extract data.

    Data extracted here will be uploaded to BigQuery inside the `page` table on `lima-project` dataset.

    Args:
        args (sysargs): --page (-p)

    Raises:
        ValueError: Error when page is not specified
    """
    page = args.page

    crawlers = {
        "artigos": artigos.ArtigosSpider,
        "noticias": noticias.NoticiasSpider,
        "analises": analises.AnalisesSpider,
    }

    # Configure default Settings
    settings = get_project_settings()
    settings.set(
        "ITEM_PIPELINES",
        {
            "adrenaline.adrenaline.pipelines.BigqueryPipeline": 300,
        },
    )
    settings.set("BIGQUERY_PROJECT_ID", "lima-project-425805")
    settings.set("BIGQUERY_DATASET_ID", "adrenaline_transient")

    # Start extraction
    procces = CrawlerProcess(settings)
    procces.crawl(crawlers[page])
    procces.start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--page",
        "-p",
        type=str,
        required=True,
        help="Page to be loaded or extracted.",
    )

    args = parser.parse_args()

    main(args)
