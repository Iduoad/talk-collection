from argparse import Namespace
from typing import Dict, List
from helpers import split_list, has_common_tags
from validate import validate, extract
import re as regex
import sys

Talk = Dict[str, str]
Talks = List[Talk]
User = str


def print_talk(talk: Talk) -> None:
    print(f"  {talk['title'].center(50)}\n")
    print(f"  {talk['type']} by {talk['talkOwner']}")
    print(f"  -> {talk['description']}")
    print(f"\n  Tags: {talk['tags']}")
    print(f"  Source: {talk['linkSource']}")
    print(f"\n  File path: {talk['filePath']}")
    print(f"\n{'-' * 60}")


def fetch_tags(db: Dict[str, Dict[User, Talks]], args: Namespace) -> None:
    if args.list:
        print('Available tags are:')
        for chunk in split_list(db['tags'], 3):
            for tag in chunk:
                print(f" # {tag:20}", end="")
            print()


def fetch_talks(db: Dict[str, Dict[User, Talks]], args: Namespace) -> None:
    for user, talks in db['talks'].items():
        for talk in talks:
            if args.tags and args.user:
                if regex.search(args.title, talk['title'])\
                  and has_common_tags(talk['tags'], args.tags)\
                  and args.user == user:
                    print_talk(talk)
            elif args.user and args.tags is None:
                if regex.search(args.title, talk['title'])\
                  and args.user == user:
                    print_talk(talk)
            elif args.tags and args.user is None:
                if regex.search(args.title, talk['title'])\
                   and has_common_tags(talk['tags'], args.tags):
                    print_talk(talk)
            else:
                if regex.search(args.title, talk['title']):
                    print_talk(talk)


def fetch_users(db: Dict[str, Dict[User, Talks]], args: Namespace) -> None:
    if args.list:
        print('Available users are:')
        for chunk in split_list(list(db['talks'].keys()), 3):
            for user in chunk:
                print(f" # {user:20}", end="")
            print()


def validate_note(db: Dict[str, Dict[User, Talks]], args: Namespace) -> None:
    for filename in args.file:
        with filename as file:
            if not validate(extract(file)):
                sys.exit(1)
    sys.exit(0)


def submit_note(db: Dict[str, Dict[User, Talks]], args: Namespace) -> None:
    print('Work in progress ...')
