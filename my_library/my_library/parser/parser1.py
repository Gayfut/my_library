from time import sleep

from base_parser import BaseParser
from parser_settings import (
    _2lib_link_to_get_site,
    _2lib_get_site_selector,
    _2lib_search_margin_selector,
    _2lib_search_button_selector,
    _2lib_book_element_selector,
    _2lib_name_selector,
    _2lib_author_selector,
    _2lib_description_selector,
    _2lib_img_selector,
    _2lib_download_link_selector,
)


class Parser1(BaseParser):

    LINK_TO_SITE = None
    SEARCH_MARGIN_SELECTOR = _2lib_search_margin_selector
    SEARCH_BUTTON_SELECTOR = _2lib_search_button_selector
    BOOK_ELEMENT_SELECTOR = _2lib_book_element_selector
    NAME_SELECTOR = _2lib_name_selector
    AUTHOR_SELECTOR = _2lib_author_selector
    DESCRIPTION_SELECTOR = _2lib_description_selector
    IMG_SELECTOR = _2lib_img_selector
    DOWNLOAD_LINK_SELECTOR = _2lib_download_link_selector

    def start_parse(self, search_query):
        self.__get_link_to_site()
        self._open_site()
        self._search_in_site(search_query)

        books_links = self._get_links()
        books_info = self._get_books_info(books_links)
        print(books_info)

    def __get_link_to_site(self):
        self._browser.get(_2lib_link_to_get_site)

        sleep(10)

        self.LINK_TO_SITE = self._browser.find_element_by_css_selector(
            _2lib_get_site_selector
        ).text
        self.LINK_TO_SITE = "https://" + self.LINK_TO_SITE
