"""
Main Application Class: Create a NoteApplication class that serves as the main entry point of the application.
This class should instantiate the NoteRepository and handle command-line arguments.
"""
import sys
from datetime import datetime

from input_parser import Parser
from note_repository import NoteRepository


class MainApplication:
    def __init__(self):
        self.repo = NoteRepository("notes.json")

    def run(self, args: list):
        parsed_args = Parser.parse_args(args[1:])
        date_filter = None

        if parsed_args.date:
            try:
                date_filter = datetime.strptime(parsed_args.date, "%Y-%m-%d")
            except ValueError:
                print("The date format is incorrect! There will be no filtering by date.")

        if parsed_args.add:
            self.repo.add_note()
            print("Note added successfully.")
        elif parsed_args.list:
            self.repo.list_notes(date_filter)
        elif parsed_args.delete:
            self.repo.list_notes(date_filter)
            self.repo.delete_note()
        elif parsed_args.edit:
            self.repo.list_notes(date_filter)
            self.repo.edit_note()
        else:
            print("Usage: python notes.py [--add/--list/--delete/--edit]")

        self.repo.save()


if __name__ == "__main__":
    app = MainApplication()
    app.run(sys.argv)
