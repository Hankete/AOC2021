import os
from typing import List


def parse(file_name: str) -> List[str]:
    with open(os.path.dirname(__file__) + f"/inputs/{file_name}") as reader:
        line = reader.readline()
        result = []
        while line != "":  # The EOF char is an empty string
            #print(line, end="")
            line = reader.readline()
            result.append(line.rstrip("\n"))
        return result[:-1]


def convert_list_to_int(list_str: List[str]) -> List[int]:
    return [int(elem) for elem in list_str]


def convert_list_to_float(list_str: List[str]) -> List[float]:
    return [float(elem) for elem in list_str]


def split_list(list_str: List[str]) -> List[List[str]]:
    return [elem.split(sep=" ") for elem in list_str]

