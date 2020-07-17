import time
import os
import re
import json

if not os.path.exists("languagepacks"):
    raise FileNotFoundError


def dict_of_all_languages():
    languages_dict = dict()

    #  checking for valid files
    pattern = r"\d+_.+\.json"
    for file_name in os.listdir("languagepacks"):
        if re.match(pattern, file_name):
            file_index = file_name.split("_")[0]
            name = file_name.split("_")[1].split(".")[0]
            languages_dict[int(file_index)] = name
    return languages_dict


def extract_language_pack(index):
    #  checking for valid files
    pattern = r"\d+_.+\.json"
    for file_name in os.listdir("languagepacks"):
        if re.match(pattern, file_name):

            file_index = file_name.split("_")[0]
            if index == int(file_index):

                with open("languagepacks/" + file_name, encoding="utf-8") as f:
                    text = json.load(f)
                    f.close()
                    return text
    return IndexError


if __name__ == "__main__":
    print("You picked wrong house, fool!")
    time.sleep(2)
