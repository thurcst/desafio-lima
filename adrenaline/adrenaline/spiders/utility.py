from bs4 import BeautifulSoup
import scrapy


def clean_data(data: list | str) -> dict:
    """To clean this data will be necessary only remove whitespaces from the beginning and end.

    Args:
        data (dict): data to be clean

    Returns:
        data (dict): cleaned data
    """

    if isinstance(data, list):
        data = [x.strip() for x in data]
    else:
        data = data.strip()

    return data


def clean_text(element: scrapy.Selector) -> str:
    """Extract text from element using Beautiful soup

    Args:
        element (scrapy.Selector): Selector element with text

    Returns:
        str: Text extracted from Selector
    """
    sopa = BeautifulSoup(element.get(), "html.parser")

    # Removing all text from images (alt and titles)
    for img in sopa.find_all("img"):
        if img.has_attr("alt"):
            del img["alt"]
        if img.has_attr("title"):
            del img["title"]

    # Removing all image captions
    for figcaption in sopa.find_all("figcaption"):
        figcaption.decompose()

    return sopa.get_text()
