"""file with template-parent for parsers"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)
from itertools import groupby

from .parser_settings import (
    book_link_attribute,
    img_link_attribute,
    download_link_attribute,
    book_base_img,
)


class BaseParser:
    """control template-parent for parsers"""

    LINK_TO_SITE = None
    SEARCH_MARGIN_SELECTOR = None
    SEARCH_BUTTON_SELECTOR = None
    BOOK_ELEMENT_SELECTOR = None
    NAME_SELECTOR = None
    AUTHOR_SELECTOR = None
    DESCRIPTION_SELECTOR = None
    IMG_SELECTOR = None
    DOWNLOAD_LINK_SELECTOR = None

    def __init__(self):
        self._browser = webdriver.Firefox(options=self.__set_options())
        self.__main_window = None

    @staticmethod
    def __set_options():
        """return headless options for parser driver"""
        options = Options()
        options.add_argument("--headless")

        return options

    def start_parse(self, search_query):
        """start parsing step by step"""
        self._open_site()
        sleep(1)
        self._search_in_site(search_query)
        sleep(1)

        books_links = self._get_links()
        try:
            books_info = self._get_books_info(books_links)
        except IndexError:
            books_info = []

        return books_info

    def _open_site(self):
        """open site for parsing"""
        self._browser.get(self.LINK_TO_SITE)
        self.__main_window = self._browser.current_window_handle

    def _search_in_site(self, search_query):
        """find search margin, send request and submit"""
        search_margin = self._browser.find_element_by_css_selector(
            self.SEARCH_MARGIN_SELECTOR
        )
        search_margin.clear()
        search_margin.send_keys(search_query)

        search_button = self._browser.find_element_by_css_selector(
            self.SEARCH_BUTTON_SELECTOR
        )
        try:
            search_button.click()
        except ElementNotInteractableException:
            search_margin.submit()

    def _get_links(self):
        """find elements and return books links"""
        books_elements = self._browser.find_elements_by_css_selector(
            self.BOOK_ELEMENT_SELECTOR
        )
        books_links = []

        for book_element in books_elements:
            book_link = book_element.get_attribute(book_link_attribute)
            books_links.append(book_link)

        books_links = [link for link, _ in groupby(books_links)]
        books_links = books_links[:10]

        return books_links

    def _get_books_info(self, books_links):
        """open new tab, parse links and return info about books"""
        books_info = []

        self._browser.execute_script("window.open('');")
        self._browser.switch_to.window(self._browser.window_handles[1])

        for link_to_book in books_links:
            book_info = self.__get_book_info(link_to_book)
            books_info.append(book_info)

        self._browser.close()
        self._browser.switch_to.window(self._browser.window_handles[0])

        return books_info

    def __get_book_info(self, link_to_book):
        """return info about definite book"""
        self._browser.get(link_to_book)

        try:
            author = self._browser.find_element_by_css_selector(
                self.AUTHOR_SELECTOR
            ).text
        except NoSuchElementException:
            author = "No Author"

        try:
            description = self._browser.find_element_by_css_selector(
                self.DESCRIPTION_SELECTOR
            ).text
        except NoSuchElementException:
            description = "No description"

        try:
            img_link = self._browser.find_element_by_css_selector(
                self.IMG_SELECTOR
            ).get_attribute(img_link_attribute)
        except NoSuchElementException:
            img_link = book_base_img

        try:
            download_link = self._browser.find_element_by_css_selector(
                self.DOWNLOAD_LINK_SELECTOR
            ).get_attribute(download_link_attribute)
        except NoSuchElementException:
            download_link = "Link deleted by legal owner"

        book_info = {
            "name": self._browser.find_element_by_css_selector(self.NAME_SELECTOR).text,
            "author": author,
            "description": description,
            "img_link": img_link,
            "link": link_to_book,
            "download_link": download_link,
        }

        return book_info

    def stop_parse(self):
        """stop parsing"""
        self._browser.quit()
