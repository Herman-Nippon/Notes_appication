"""
Note Class: Create a Note class to represent individual notes.
This class should encapsulate the properties of a note (such as id, title, body, timestamp)
and provide methods for editing and deleting notes.
"""
from datetime import datetime


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
