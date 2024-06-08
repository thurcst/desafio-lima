from bs4 import BeautifulSoup
import scrapy.http
import scrapy


class NoticiasSpider(scrapy.Spider):
    name = "noticias"
    allowed_domains = ["www.adrenaline.com.br"]
    start_urls = ["http://www.adrenaline.com.br/noticias/"]

    def parse(self, response):
        articles = response.css("div.archive-list-posts article.feed")

        for article in articles:
            first_anchor = article.css("a::attr(href)").get()
            title = article.css("h2.feed-title::text").get()
            hat = response.css("p.feed-hat::text").get()
            tags = [x[1:] for x in article.css("ul.feed-tags li a::text").getall()]

            yield response.follow(
                url=first_anchor,
                callback=self.parse_article_page,
                meta={
                    "url": first_anchor,
                    "title": title,
                    "hat": hat,
                    "tags": tags,
                },
            )

    def parse_article_page(self, response: scrapy.http.Response):
        """This parser job is extract information from the article url.

        Args:
            response (scrapy.http.Response)

        Yields:
            dict: data extracted from website.
        """
        authors = []

        text_section_element = response.css("div.section-text")
        authors_element = response.css("ul.text-authors")

        text = self.parse_text(text_section_element)

        for author in authors_element:
            # The first element of those lists are, in most of times, the caracter '\n'
            # using [-1] we will extract only the last element form the array
            authors.append(author.css("li > a::text").getall()[-1])

        # variables from `parse` function context
        meta = response.request.meta

        yield {
            "url": meta["url"],
            "title": meta["title"],
            "authors": authors,
            "hat": meta["hat"],
            "tags": meta["tags"],
            "article_text": text,
        }

    def parse_text(self, element: scrapy.Selector) -> str:
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
