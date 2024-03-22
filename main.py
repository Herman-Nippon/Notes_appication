import json
import os
import sys
from datetime import datetime

NOTES_FILE = "notes.json"


def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    else:
        return []


def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)


def add_note(notes):
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"id": notes[-1]['id'] + 1 if notes else 1, "title": title, "body": body, "timestamp": timestamp}


def list_notes(notes):
    if notes:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Timestamp: {note['timestamp']}")
            print()
    else:
        print("No notes available.")


def delete_note(notes):
    list_notes(notes)
    if notes:
        note_id = int(input("Enter the ID of the note to delete: "))
        for note in notes:
            if note["id"] == note_id:
                notes.remove(note)
                print("Note deleted successfully.")
                break
        else:
            print("Invalid note ID.")
        save_notes(notes)


def edit_note(notes):
    list_notes(notes)
    if notes:
        note_id = int(input("Enter the ID of the note to edit: "))
        for i, note in enumerate(notes):
            if note["id"] == note_id:
                note_index = i
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
        print(f"ID: {notes[note_index]['id']}")
        if to_change in ["title", "both"]:
            notes[note_index]["title"] = input(f"Enter new title (previous: {notes[note_index]['title']}): ")
        if to_change in ["body", "both"]:
            notes[note_index]["body"] = input(f"Enter new body (previous: {notes[note_index]['body']}): ")
        notes[note_index]["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Note edited successfully.")
        save_notes(notes)


def main():
    notes = load_notes()

    if len(sys.argv) < 2:
        print("Usage: python notes.py [--add/--list/--delete/--edit]")
        return

    if sys.argv[1] == "--add":
        note = add_note(notes)
        notes.append(note)
        save_notes(notes)
        print("Note added successfully.")
    elif sys.argv[1] == "--list":
        list_notes(notes)
    elif sys.argv[1] == "--delete":
        delete_note(notes)
    elif sys.argv[1] == "--edit":
        edit_note(notes)
    else:
        print("Usage: python notes.py [--add/--list/--delete/--edit]")


if __name__ == "__main__":
    main()
