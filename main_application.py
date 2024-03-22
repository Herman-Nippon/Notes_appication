"""
Main Application Class: Create a NoteApplication class that serves as the main entry point of the application.
This class should instantiate the NoteRepository and handle command-line arguments.
"""
import sys

from note_repository import NoteRepository


class MainApplication:
    def __init__(self):
        self.repo = NoteRepository("notes.json")

    def run(self, args: list):
        if len(args) < 2:
            print("Usage: python notes.py [--add/--list/--delete/--edit]")
            return

        if args[1] == "--add":
            self.repo.add_note()
            print("Note added successfully.")
        elif args[1] == "--list":
            self.repo.list_notes()
        elif args[1] == "--delete":
            self.repo.list_notes()
            self.repo.delete_note()
        elif args[1] == "--edit":
            self.repo.list_notes()
            self.repo.edit_note()
        else:
            print("Usage: python notes.py [--add/--list/--delete/--edit]")

        self.repo.save()


if __name__ == "__main__":
    app = MainApplication()
    app.run(sys.argv)
