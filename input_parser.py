import argparse


class Parser:
    @staticmethod
    def parse_args(args):
        parser = argparse.ArgumentParser(prog="Notes++",
                                         description="The application for note-taking.")
        parser.add_argument("--add", action="store_true", help="Add a new note")
        parser.add_argument("--list", action="store_true", help="List all notes")
        parser.add_argument("--delete", action="store_true", help="Delete a note")
        parser.add_argument("--edit", action="store_true", help="Edit a note")
        parser.add_argument("--date", type=str, help="Filter notes by date (format: YYYY-MM-DD)")

        return parser.parse_args(args)
