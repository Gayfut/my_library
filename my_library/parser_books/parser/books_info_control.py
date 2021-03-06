"""file for control parsed books info saving in json and loading from json"""
import json
import os

from .parser_settings import books_info_dir


def save_info(books_info, info_number, username):
    """save books info in json file"""
    try:
        with open(books_info_dir + "/books_info" + str(info_number) + "_" + str(username) + ".json", "w", encoding="utf-8") as file_with_info:
            json.dump(books_info, file_with_info, ensure_ascii=False)
    except FileNotFoundError:
        os.mkdir(books_info_dir)
        with open(books_info_dir + "/books_info" + str(info_number) + "_" + str(username) + ".json", "w", encoding="utf-8") as file_with_info:
            json.dump(books_info, file_with_info, ensure_ascii=False)


def load_info(info_number, username):
    """load info from json file"""
    try:
        with open(books_info_dir + "/books_info" + str(info_number) + "_" + str(username) + ".json", encoding="utf-8") as file_with_info:
            books_info = json.load(file_with_info)
    except FileNotFoundError:
        books_info = []

    return books_info
