import argparse

from greetings import build_greeting


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple multilingual greeting")
    parser.add_argument("name", nargs="?", default="φίλε", help="Name to greet")
    parser.add_argument(
        "-l",
        "--language",
        choices=["el", "en", "es"],
        default="el",
        help="Language code for the greeting (el, en, es)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    message = build_greeting(name=args.name, language=args.language)
    print(f"{message} Αυτό είναι το πρώτο μου Python πρόγραμμα 🐍")


if __name__ == "__main__":
    main()
