import argparse

"""
Parser class:
This class provides a static method to parse command-line arguments for the Notes++ application. 
It utilizes the argparse module to define and parse command-line options.

Methods:
- parse_args(args): 
    Static method that accepts a list of command-line arguments and parses them using the argparse module.
  
Description of Arguments:
- --add: Specifies to add a new note to the application.
- --list: Specifies to list all notes stored in the application.
- --delete: Specifies to delete a note from the application.
- --edit: Specifies to edit an existing note in the application.
- --date: Optional argument to filter notes by a specific date (format: YYYY-MM-DD).
"""

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
