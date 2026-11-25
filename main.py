#!/usr/bin/env python3
"""Office joke entry: writes one single-line office joke to /output/entry.txt.

Winner of an internal 10-variant pairwise tournament (4 wins):
beat the smaller-box joke, the Wi-Fi/HR joke, the reply-all chain joke,
and the 'per my last email' will joke.
"""

import os

JOKE = "I asked for a raise and got a pizza party, so now I technically earn 12% more pepperoni."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8, 1-200 chars, exactly one line.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
