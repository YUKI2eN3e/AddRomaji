#!/usr/bin/env python3
import argparse
import os
import urllib.request
from dataclasses import dataclass

FULL_DICT_URL = "ftp://ftp.edrdg.org/pub/Nihongo//JMdict.gz"
EN_DICT_URL = "ftp://ftp.edrdg.org/pub/Nihongo//JMdict_e.gz"


@dataclass
class CliArgs:
    full: bool
    english: bool


def get_args() -> CliArgs:
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__).removesuffix(".py")
    )
    parser.add_argument(
        "-f",
        "--full",
        help="Download Full JMdict file.",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-e",
        "--english",
        help="Download English JMdict file.",
        action="store_true",
        default=False,
    )
    return CliArgs(**vars(parser.parse_args()))


def download_file(file_url: str):
    file_name = file_url.split("/")[-1]
    urllib.request.urlretrieve(file_url, file_name)
    return file_name


def run():
    args = get_args()
    if args.full:
        full_file = download_file(FULL_DICT_URL)
        print("Downloaded Full JMdict as: {}".format(full_file))
    if args.english:
        english_file = download_file(EN_DICT_URL)
        print("Downloaded English JMdict as: {}".format(english_file))


if __name__ == "__main__":
    run()
