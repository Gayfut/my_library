"""file for control parser2 and his specification"""
from .base_parser import BaseParser
from .parser_settings import (
    _2_link_to_site,
    _2_search_margin_selector,
    _2_search_button_selector,
    _2_book_element_selector,
    _2_name_selector,
    _2_author_selector,
    _2_description_selector,
    _2_img_selector,
    _2_download_link_selector,
)


class Parser2(BaseParser):
    """control parser2"""

    LINK_TO_SITE = _2_link_to_site
    SEARCH_MARGIN_SELECTOR = _2_search_margin_selector
    SEARCH_BUTTON_SELECTOR = _2_search_button_selector
    BOOK_ELEMENT_SELECTOR = _2_book_element_selector
    NAME_SELECTOR = _2_name_selector
    AUTHOR_SELECTOR = _2_author_selector
    DESCRIPTION_SELECTOR = _2_description_selector
    IMG_SELECTOR = _2_img_selector
    DOWNLOAD_LINK_SELECTOR = _2_download_link_selector
