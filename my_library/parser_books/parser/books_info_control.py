import json
import os

from .parser_settings import books_info_dir


def save_info(books_info1, books_info2, books_info3):
    try:
        with open(books_info_dir + "/books_info1.json", "w", encoding="utf-8") as file_with_info:
            json.dump(books_info1, file_with_info, ensure_ascii=False)
    except FileNotFoundError:
        os.mkdir(books_info_dir)
        with open(books_info_dir + "/books_info1.json", "w", encoding="utf-8") as file_with_info:
            json.dump(books_info1, file_with_info, ensure_ascii=False)

    try:
        with open(books_info_dir + "/books_info2.json", "w", encoding="utf-8") as file_with_info:
            json.dump(books_info2, file_with_info, ensure_ascii=False)
    except FileNotFoundError:
        os.mkdir(books_info_dir)
        with open(books_info_dir + "/books_info2.json", "w", encoding="utf-8") as file_with_info:
            json.dump(books_info2, file_with_info, ensure_ascii=False)

    try:
        with open(books_info_dir + "/books_info3.json", "w", encoding="utf-8") as file_with_info:
            json.dump(books_info3, file_with_info, ensure_ascii=False)
    except FileNotFoundError:
        os.mkdir(books_info_dir)
        with open(books_info_dir + "/books_info3.json", "w", encoding="utf-8") as file_with_info:
            json.dump(books_info3, file_with_info, ensure_ascii=False)


def load_info():
    try:
        with open(books_info_dir + "/books_info1.json", encoding="utf-8") as file_with_info:
            books_info1 = json.load(file_with_info)
    except FileNotFoundError:
        books_info1 = []

    try:
        with open(books_info_dir + "/books_info2.json", encoding="utf-8") as file_with_info:
            books_info2 = json.load(file_with_info)
    except FileNotFoundError:
        books_info2 = []

    try:
        with open(books_info_dir + "/books_info3.json", encoding="utf-8") as file_with_info:
            books_info3 = json.load(file_with_info)
    except FileNotFoundError:
        books_info3 = []

    return books_info1, books_info2, books_info3
