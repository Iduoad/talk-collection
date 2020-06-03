from typing import List, Dict, Iterator
from os import path
import json


def read_json(file_path: str) -> str:
    """Read a JSON file."""

    try:
        with open(path.abspath(file_path), mode='r', encoding='UTF-8') as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return {}


def write_json(dic: Dict[any, any], file_path: str) -> str:
    """Convert a dictionary to a JSON file."""

    with open(path.abspath(file_path), mode='w', encoding='UTF-8') as file:
        json.dump(dic, file, indent=4)


def split_list(alist: List[any], chunkSize: int) -> Iterator[any]:
    """Split a list into chunks.
       Example: ([3, 4, 5, 6], 2) == [[3, 4], [5, 6]]
    """
    n = max(1, chunkSize)
    return (alist[i:i+n] for i in range(0, len(alist), n))


def has_common_tags(talk_tags: List[str],
                    args_tags: List[str],
                    ignore_case: bool = True) -> bool:
    """Checks if two lists has elements in common.
       Example: ([1, 2], [2]) == True / ([3, 4], [5, 6]) == False
    """
    talk_tags = set(map(str.lower, talk_tags)) if ignore_case else talk_tags
    args_tags = set(map(str.lower, args_tags)) if ignore_case else args_tags
    return len(talk_tags.intersection(args_tags)) > 0
