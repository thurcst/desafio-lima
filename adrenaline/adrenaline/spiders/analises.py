from adrenaline.adrenaline.spiders.utility import clean_data, clean_text
from adrenaline.adrenaline.items import AdrenalineItem

import scrapy.http
import scrapy


class AnalisesSpider(scrapy.Spider):
    name = "analises"
    allowed_domains = ["www.adrenaline.com.br"]
    start_urls = ["http://www.adrenaline.com.br/analises/"]

    def parse(self, response: scrapy.http.Response):
        articles = response.css("div.archive-list-posts article.feed")

        for article in articles:

            item = AdrenalineItem()

            # Iterando na lista de articles da página
            first_anchor = article.css("a::attr(href)").get()
            title = article.css("h2.feed-title::text").get()
            hat = response.css("p.feed-hat::text").get()
            tags = [x[1:] for x in article.css("ul.feed-tags li a::text").getall()]

            # Limpeza de dados
            item["url"] = clean_data(first_anchor)
            item["title"] = clean_data(title)
            item["hat"] = clean_data(hat)
            item["tags"] = clean_data(tags)

            yield response.follow(
                url=first_anchor, callback=self.parse_article_page, meta={"item": item}
            )

    def parse_article_page(self, response: scrapy.Selector):
        """This parser job is extract information from the article url.

        Args:
            response (scrapy.Selector)

        Yields:
            dict: data extracted from website.
        """
        item = response.request.meta["item"]

        authors = []

        text_section_element = response.css("div.section-text")
        authors_element = response.css("ul.text-authors")

        text = clean_text(text_section_element)

        for author in authors_element:
            # The first element of those lists are, in most of times, the caracter '\n'
            # using [-1] we will extract only the last element form the array
            authors.append(author.css("li > a::text").getall()[-1].strip())

        item["authors"] = clean_data(authors)
        item["text"] = text

        yield item
