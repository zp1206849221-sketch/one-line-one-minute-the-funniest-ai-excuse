"""Write the one-line AI excuse entry to /output/entry.txt."""

import os

ENTRY = "Sorry I'm late: I hallucinated a later deadline, cited three papers that don't exist to defend it, and delivered the report, confidently, to last Tuesday."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
