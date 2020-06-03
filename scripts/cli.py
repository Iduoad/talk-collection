from argparse import Namespace
from typing import Dict, List
from helpers import split_list, has_common_tags
from validate import validate, extract
import re as regex
import sys

# Define aliases for readability
Talk = Dict[str, str]
Talks = List[Talk]
User = str


def print_talk(talk: Talk) -> None:
    """Display information about the talk."""

    print(f"  {talk['title'].center(50)}\n")
    print(f"  {talk['type']} by {talk['talkOwner']}")
    print(f"  -> {talk['description']}")
    print(f"\n  Tags: {talk['tags']}")
    print(f"  Source: {talk['linkSource']}")
    print(f"\n  File path: {talk['filePath']}")
    print(f"\n{'-' * 60}")


def fetch_tags(db: Dict[str, Dict[User, Talks]], args: Namespace) -> None:
    """Display available tags in database."""

    if args.list:
        # find tags / find tags -ls / find tags --list
        print('Available tags are:')

        # Print tags in columns
        for chunk in split_list(db['tags'], 3):
            for tag in chunk:
                print(f" # {tag:20}", end="")
            print()


def fetch_talks(db: Dict[str, Dict[User, Talks]], args: Namespace) -> None:
    """Fetch talks from database and display them."""

    for user, talks in db['talks'].items():
        for talk in talks:
            # find talks --title .. --user .. --tags ..
            if args.tags and args.user:
                if regex.search(args.title, talk['title'])\
                  and has_common_tags(talk['tags'], args.tags)\
                  and args.user == user:
                    print_talk(talk)
            # find talks --title .. --user ..
            elif args.user and args.tags is None:
                if regex.search(args.title, talk['title'])\
                  and args.user == user:
                    print_talk(talk)
            # find talks --title .. --tags ..
            elif args.tags and args.user is None:
                if regex.search(args.title, talk['title'])\
                   and has_common_tags(talk['tags'], args.tags):
                    print_talk(talk)
            else:
                # find talks --title ..
                if regex.search(args.title, talk['title']):
                    print_talk(talk)


def fetch_users(db: Dict[str, Dict[User, Talks]], args: Namespace) -> None:
    """Fetch users from database and display their usernames."""

    if args.list:
        # find users / find users -ls / find users --list
        print('Available users are:')

        # Print usernames in columns
        for chunk in split_list(list(db['talks'].keys()), 3):
            for user in chunk:
                print(f" # {user:20}", end="")
            print()


def validate_note(db: Dict[str, Dict[User, Talks]], args: Namespace) -> None:
    """Verify if the note contains required metadata."""

    # validate --file .. .. ..
    for filename in args.file:
        with filename as file:
            if not validate(extract(file)):
                sys.exit(1)
    sys.exit(0)


def submit_note(db: Dict[str, Dict[User, Talks]], args: Namespace) -> None:
    print('Work in progress ...')
