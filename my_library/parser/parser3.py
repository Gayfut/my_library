"""file for control parser3 and his specification"""
from base_parser import BaseParser
from parser_settings import (
    _3_link_to_site,
    _3_search_margin_selector,
    _3_search_button_selector,
    _3_book_element_selector,
    _3_name_selector,
    _3_author_selector,
    _3_description_selector,
    _3_img_selector,
    _3_download_link_selector,
)


class Parser3(BaseParser):
    """control parser3"""

    LINK_TO_SITE = _3_link_to_site
    SEARCH_MARGIN_SELECTOR = _3_search_margin_selector
    SEARCH_BUTTON_SELECTOR = _3_search_button_selector
    BOOK_ELEMENT_SELECTOR = _3_book_element_selector
    NAME_SELECTOR = _3_name_selector
    AUTHOR_SELECTOR = _3_author_selector
    DESCRIPTION_SELECTOR = _3_description_selector
    IMG_SELECTOR = _3_img_selector
    DOWNLOAD_LINK_SELECTOR = _3_download_link_selector
