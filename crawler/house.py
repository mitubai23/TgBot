import httpx
from parsel import Selector
from pprint import pprint
import asyncio


class HouseCrawler:
    MAIN_URL = "https://www.house.kg/snyat"
    BASE_URL = "https://www.house.kg"

    def get_page(self):
        response = httpx.get(self.MAIN_URL)
        print("Status code: ", response.status_code)
        return response.text

    def get_title(self, html):
        selector = Selector(text=html)
        return selector.css("h1::text").get()

    def get_links(self, html):
        selector = Selector(text=html)
        links = selector.css("div.left-image a::attr(href)").getall()
        links = list(map(lambda x: self.BASE_URL + x, links))
        return links


if __name__ == "__main__":
    crawler = HouseCrawler()
    page = crawler.get_page()
    links = crawler.get_links(page)
    pprint(links)