import json
import os

from .parser_settings import books_info_dir


def save_info(books_info, info_number):
    try:
        with open(books_info_dir + "/books_info" + str(info_number) + ".json", "w", encoding="utf-8") as file_with_info:
            json.dump(books_info, file_with_info, ensure_ascii=False)
    except FileNotFoundError:
        os.mkdir(books_info_dir)
        with open(books_info_dir + "/books_info" + str(info_number) + ".json", "w", encoding="utf-8") as file_with_info:
            json.dump(books_info, file_with_info, ensure_ascii=False)


def load_info(info_number):
    try:
        with open(books_info_dir + "/books_info" + str(info_number) + ".json", encoding="utf-8") as file_with_info:
            books_info = json.load(file_with_info)
    except FileNotFoundError:
        books_info = []

    return books_info
