"""
NoteRepository Class: Create a NoteRepository class responsible for loading, saving, adding, listing, deleting,
and editing notes.
This class should handle interactions with the storage (in this case, JSON notes_file) and manage the
collection of notes.
"""
import json
import os
from note import Note


class NoteRepository:
    def __init__(self, notes_file: str):
        self.notes_file = notes_file
        self.notes_list: list[Note] = self.load()

    def load(self):
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

    def list_notes(self):
        if self.notes_list:
            for note in self.notes_list:
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
