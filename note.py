from datetime import datetime

"""
Note class: 
This class manages individual notes within a note-taking system.

Fields:
- id: An integer representing the unique identifier of the note.
- title: A string containing the title of the note.
- body: A string containing the main content or body of the note.
- timestamp: A string representing the timestamp of the note's creation or last modification.

Methods:
- __init__: 
    Initializes a note object.
    
- edit: 
    Modifies the title and/or body of the note and updates the timestamp to reflect the modification time.
    
- match_id -> bool: 
    Compares the provided note ID with the ID of the current note and returns True if they match, False otherwise.
    
- __repr__: 
    Returns a string representation of the note, including its ID, title, body, and timestamp.
"""


class Note:
    def __init__(self, id: int, title: str = None, body: str = None, timestamp: str = None):
        self.id = id
        self.title = input("Enter note title: ") if not title else title
        self.body = input("Enter note body: ") if not body else body
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if not timestamp else timestamp

    def edit(self, title: str = None, body: str = None):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if title:
            self.title = title
        if body:
            self.body = body

    def match_id(self, note_id: int) -> bool:
        return note_id == self.id

    def __repr__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nBody: {self.body}\nLast modified: {self.timestamp}\n"
