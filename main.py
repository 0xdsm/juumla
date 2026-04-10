#!/usr/bin/env python3

import sys
from argparse import ArgumentParser

from src.interface.ui import get_banner
from src.juumla.main import perform_checks
from src.juumla.settings import build_session


def parse_custom_headers(raw_headers: list[str] | None) -> dict[str, str]:
    if not raw_headers:
        return {}

    headers: dict[str, str] = {}
    for entry in raw_headers:
        if ":" not in entry:
            print(f"[-] Invalid header format (expected 'Name: Value'): {entry}")
            sys.exit(1)
        name, _, value = entry.partition(":")
        headers[name.strip()] = value.strip()

    return headers


if __name__ == "__main__":
    get_banner()

    parser = ArgumentParser()
    parser.add_argument(
        "-u",
        help="-u: HTTP(s) target URL to run the scanner",
        required=True,
    )
    parser.add_argument(
        "-H",
        help="-H: Custom header in 'Name: Value' format (can be used multiple times)",
        action="append",
        dest="headers",
        metavar="HEADER",
    )
    args = parser.parse_args()

    custom_headers = parse_custom_headers(args.headers)
    session = build_session(custom_headers)

    perform_checks(args.u, session)
