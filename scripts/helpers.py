from typing import List, Dict, Iterator
from os import path
import json


def read_json(file_path: str) -> str:
    try:
        with open(path.abspath(file_path), mode='r', encoding='UTF-8') as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return {}


def write_json(dic: Dict[any, any], file_path: str) -> str:
    with open(path.abspath(file_path), mode='w', encoding='UTF-8') as file:
        json.dump(dic, file, indent=4)


def split_list(alist: List[any], chunkSize: int) -> Iterator[any]:
    n = max(1, chunkSize)
    return (alist[i:i+n] for i in range(0, len(alist), n))


def has_common_tags(talk_tags: List[str],
                    args_tags: List[str],
                    ignore_case: bool = True) -> bool:
    talk_tags = set(map(str.lower, talk_tags)) if ignore_case else talk_tags
    args_tags = set(map(str.lower, args_tags)) if ignore_case else args_tags
    return len(talk_tags.intersection(args_tags)) > 0
