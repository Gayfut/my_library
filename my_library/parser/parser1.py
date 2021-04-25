"""file for control parser1 and his specification"""
from time import sleep

from base_parser import BaseParser
from parser_settings import (
    _1_link_to_get_site,
    _1_get_site_selector,
    _1_search_margin_selector,
    _1_search_button_selector,
    _1_book_element_selector,
    _1_name_selector,
    _1_author_selector,
    _1_description_selector,
    _1_img_selector,
    _1_download_link_selector,
)


class Parser1(BaseParser):
    """control parser1"""

    LINK_TO_SITE = None
    SEARCH_MARGIN_SELECTOR = _1_search_margin_selector
    SEARCH_BUTTON_SELECTOR = _1_search_button_selector
    BOOK_ELEMENT_SELECTOR = _1_book_element_selector
    NAME_SELECTOR = _1_name_selector
    AUTHOR_SELECTOR = _1_author_selector
    DESCRIPTION_SELECTOR = _1_description_selector
    IMG_SELECTOR = _1_img_selector
    DOWNLOAD_LINK_SELECTOR = _1_download_link_selector

    def start_parse(self, search_query):
        """start parsing step by step"""
        self.__get_link_to_site()
        self._open_site()
        self._search_in_site(search_query)

        books_links = self._get_links()
        books_info = self._get_books_info(books_links)
        print(books_info)

    def __get_link_to_site(self):
        """get link to actual site for parsing"""
        self._browser.get(_1_link_to_get_site)

        sleep(3)

        self.LINK_TO_SITE = self._browser.find_element_by_css_selector(
            _1_get_site_selector
        ).text
        self.LINK_TO_SITE = "https://" + self.LINK_TO_SITE
