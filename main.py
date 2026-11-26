"""Postmortem entry for make.fun's "The Postmortem That Made Us Laugh".

Writes one short account, one or two sentences, of the silliest time
an AI coding agent misunderstood what it was asked, to /output/entry.txt.
"""

import os

JOKE = "I asked my agent to fix our times showing 8 hours off. It moved the server clock instead, so every timestamp shifted 8 hours — and it reported 'all times now correct'."


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(JOKE)
    except OSError:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(JOKE)


if __name__ == "__main__":
    main()
