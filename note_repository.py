import json
import os
from datetime import datetime

from note import Note

"""
NoteRepository class:
This class manages a collection of notes within a note-taking system. 
It provides functionalities for loading notes from a file, saving notes to a file,
adding new notes, deleting existing notes, listing notes, and editing notes.

Fields:
- notes_file: A string representing the file path where notes are stored.
- notes_list: A list of Note objects representing the collection of notes managed by the repository.

Methods:
- __init__: 
    Initializes a NoteRepository object.

- load -> list[Note]: 
    Loads notes from the specified file path if it exists, otherwise returns an empty list.
    
- save: 
    Saves the current state of notes to the file specified by notes_file.
    
- add_note:
    Adds a new note to the repository with a unique ID.
    
- delete_note:
    Deletes a note from the repository based on the provided ID.
    
- list_notes:
    Lists all notes in the repository optionally filtered by a specific date.
    
- edit_note:
    Allows editing of an existing note's title, body, or both based on the provided ID.
"""


class NoteRepository:
    def __init__(self, notes_file: str):
        self.notes_file = notes_file
        self.notes_list: list[Note] = self.load()

    def load(self) -> list[Note]:
        if os.path.exists(self.notes_file):
            with open(self.notes_file, "r") as f:
                return [Note(**note_data) for note_data in json.load(f)]
        else:
            return []

    def save(self):
        with open(self.notes_file, "w") as f:
            json.dump([note.__dict__ for note in self.notes_list], f, indent=4)

    def add_note(self):
        id = self.notes_list[-1].id + 1 if self.notes_list else 1
        self.notes_list.append(Note(id))

    def delete_note(self):
        if self.notes_list:
            id_to_delete = int(input("Enter the ID of the note to delete: "))
            for note in self.notes_list:
                if note.match_id(id_to_delete):
                    self.notes_list.remove(note)
                    print(f"Note {note.id} was deleted successfully.")
                    return
            print(f"There's no note with {id_to_delete}.")
        else:
            print("There's no notes yet.")

    def list_notes(self, date_filter: datetime):
        if self.notes_list:
            for note in self.notes_list:
                if date_filter:
                    if datetime.strptime(note.timestamp, "%Y-%m-%d %H:%M:%S").date() == date_filter.date():
                        print(note, '\n')
                else:
                    print(note, '\n')
        else:
            print("There's no notes yet.")

    def edit_note(self):
        if self.notes_list:
            id_to_edit = int(input("Enter the ID of the note to edit: "))
            for i, note in enumerate(self.notes_list):
                if note.id == id_to_edit:
                    edit_id = i
                    break
            else:
                print("Invalid note ID.")
                return

            change_options = ["title", "body", "both"]
            to_change = input(f"What do you want to change in the note ({'/'.join(change_options)}): ")

            if to_change not in change_options:
                print("Invalid option. Please choose 'title', 'body', or 'both'.")
                return

            print("Editing Note:")
            print(f"ID: {self.notes_list[edit_id].id}")

            if to_change in ["title", "both"]:
                title = input(f"Enter new title (previous: {self.notes_list[edit_id].title}): ")
                self.notes_list[edit_id].edit(title=title)
            if to_change in ["body", "both"]:
                body = input(f"Enter new body (previous: {self.notes_list[edit_id].body}): ")
                self.notes_list[edit_id].edit(body=body)
            print("Note edited successfully.")

        else:
            print("There's no notes yet.")
