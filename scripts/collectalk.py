#!/usr/bin/env python3

from argparse import ArgumentParser, FileType
from helpers import read_json
import cli


txt = {
    'prog.desc':
        'Add notes about talks and look for ones you are interested about.',
    'find': 'find talks/users/tags',
    'talks': 'find talks with custom filters',
    'talks.title': "filter by title (eg: '.* expr[ess]?', 'A title')",
    'talks.user': 'filter by user who created the notes about the talk',
    'talks.tags': 'filter by tags (eg. JavaScript, ML, ...)',
    'users': 'find users with custom filters',
    'users.list': 'list available users',
    'tags': 'find tags with custom filters',
    'tags.list': 'list available tags',
    'validate': 'validate structure of notes',
    'validate.file': 'check if the file contains required metadata',
    'submit': 'add notes about a talk'
}


parser = ArgumentParser(description=txt['prog.desc'])
parser.add_argument(
    '-v', '--version', action='version', version='%(prog)s version 1.0.0')
subparsers = parser.add_subparsers()

find_parser = subparsers.add_parser('find', help=txt['find'])
find_subparsers = find_parser.add_subparsers()
talks_parser = find_subparsers.add_parser('talks', help=txt['talks'])
talks_parser.add_argument(
    '-t', '--title', default='.*', help=txt['talks.title'], type=str)
talks_parser.add_argument('-u', '--user', help=txt['talks.user'], type=str)
talks_parser.add_argument(
    '--tags', nargs='+', help=txt['talks.tags'], type=str)
talks_parser.set_defaults(func=cli.fetch_talks)

users_parser = find_subparsers.add_parser('users', help=txt['users'])
users_parser.add_argument(
    '-ls', '--list', default=True, action='store_true', help=txt['users.list'])
users_parser.set_defaults(func=cli.fetch_users)

tags_parser = find_subparsers.add_parser('tags', help=txt['tags'])
tags_parser.add_argument(
    '-ls', '--list', default=True, action='store_true', help=txt['tags.list'])
tags_parser.set_defaults(func=cli.fetch_tags)

validate_parser = subparsers.add_parser('validate', help=txt['validate'])
validate_parser.add_argument(
    '--file', nargs='+', help=txt['validate.file'], type=FileType('r'))
validate_parser.set_defaults(func=cli.validate_note)

submit_parser = subparsers.add_parser('submit', help=txt['submit'])
submit_parser.set_defaults(func=cli.submit_note)

if __name__ == '__main__':
    db = read_json('db/talks.json')

    args = parser.parse_args()

    if 'func' in args:
        args.func(db, args)
    else:
        parser.print_help()
