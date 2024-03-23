import sys
from datetime import datetime

from input_parser import Parser
from note_repository import NoteRepository

"""
MainApplication class:
This class serves as the main interface for interacting with the note-taking application.
It processes user input, delegates actions to the NoteRepository, and manages the overall flow of the application.

Fields:
- repo: A NoteRepository object representing the repository where notes are stored.

Methods:
- __init__:
    Initializes a MainApplication object with a NoteRepository instance.
    
- run:
    Executes the application based on the provided command-line arguments.
    
- parse_args:
    Parses the command-line arguments to determine the action to be performed.
    
- add_note:
    Calls the NoteRepository's add_note method to add a new note.
    
- list_notes:
    Calls the NoteRepository's list_notes method to display notes, optionally filtered by date.
    
- delete_note:
    Calls the NoteRepository's delete_note method to delete a note.
    
- edit_note:
    Calls the NoteRepository's edit_note method to edit a note.
    
- save:
    Calls the NoteRepository's save method to persist changes to the notes file.
"""


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

        self.repo.save()


if __name__ == "__main__":
    app = MainApplication()
    app.run(sys.argv)
