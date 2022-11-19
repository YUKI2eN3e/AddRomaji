#!/usr/bin/env python3
import argparse
import pykakasi

kks = pykakasi.kakasi()

HIRAGANA_RANGE = range(0x3041, ((0x3096) + 1))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input", help="JMdict input file (JMdict_e)", required=True
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file, will use input + _r if none is provided (JMdict_e -> JMdict_e_r)",
    )
    return parser.parse_args()


def is_hiragana(text: str) -> bool:
    return ord(text.strip()[0]) in HIRAGANA_RANGE


def get_romaji(hiragana: str) -> str:
    text = ""
    for part in kks.convert(hiragana):
        text = text + part["hepburn"]
    return text


def get_formated_romaji(hiragana: str) -> list:
    text = ["<r_ele>\n", "<reb>{}</reb>\n".format(get_romaji(hiragana)), "</r_ele>\n"]
    return text


def run():
    args = get_args()
    reb = ""
    end_of_reb_ele = False
    with open(args.input, "r", encoding="utf8") as in_file:
        output = args.input + "_r"
        if args.output is not None:
            output = args.output
        with open(output, "w", encoding="utf8") as out_file:
            for line in in_file.readlines():
                if end_of_reb_ele:
                    try:
                        if is_hiragana(reb):
                            romaji_text = get_formated_romaji(reb)
                            out_file.writelines(romaji_text)
                    except Exception:
                        pass
                    end_of_reb_ele = False
                elif "<reb>" in line:
                    reb = line.removeprefix("<reb>").removesuffix("</reb>\n")
                elif line.strip() == "</r_ele>":
                    end_of_reb_ele = True
                out_file.write(line)


if __name__ == "__main__":
    run()
