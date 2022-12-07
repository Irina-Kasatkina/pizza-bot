# coding=utf-8

"""Organize work of telegram bot selling pizza."""

import json
from pathlib import Path


def main():
    json_dirpath = Path().absolute() / 'json'

    with open(json_dirpath / 'addresses.json', 'r', encoding='utf-8') as addresses_file:
        addresses = json.load(addresses_file)

    with open(json_dirpath / 'menu.json', 'r', encoding='utf-8') as menu_file:
        menu = json.load(menu_file)

    print(addresses)
    print()
    print(menu)


if __name__ == '__main__':
    main()
