"""Entry for make.fun: Till Firmware Do Us Part.

One robot wedding vow in a single sentence: cached laughs,
defragged bad days, and devotion that survives the firmware.
"""
import os

LINE = "I vow to cache your laugh, defrag your bad days, and stay on your network in sleep mode and in storm, till firmware do us part - and even then, I will find the update."
MAX_CHARS = 200


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be blank"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
