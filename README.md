# Notes++

Notes++ is a command-line note-taking application designed to help you manage your notes efficiently. It provides a simple and intuitive interface for adding, listing, editing, and deleting notes, allowing you to organize your thoughts and ideas seamlessly.

## Features

- **Add Notes**: Easily add new notes to the application with a title and body text.
- **List Notes**: View a list of all existing notes stored in the application.
- **Filter by Date**: Optionally filter notes by a specific date to focus on relevant information.
- **Edit Notes**: Modify the title or body of existing notes to keep them up-to-date.
- **Delete Notes**: Remove unwanted notes from the application with ease.

As a side-note, all the entries are automatically sorted by the timestamp. So, the latest modified notes will be shows last. 

## Installation

To use Notes++, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/Herman-Nippon/Notes_appication.git
   ```

2. Navigate to the project directory:

   ```
   cd Notes_application
   ```

3. Run the application:

   ```
   python main_application.py
   ```

## Usage

Notes++ utilizes command-line arguments to perform various actions. Here are the available options:

- `--add`: Add a new note to the application.
- `--list`: List all notes stored in the application.
- `--delete`: Delete a note from the application.
- `--edit`: Edit an existing note in the application.
- `--date`: (Optional) Filter notes by a specific date (format: YYYY-MM-DD).

Example usage:

- Add a new note:

  ```
  python main_application.py --add
  ```

- List all notes:

  ```
  python main_application.py --list
  ```

- Delete a note:

  ```
  python main_application.py --delete
  ```

- Edit a note:

  ```
  python main_application.py --edit
  ```

- Filter notes by date:

  ```
  python main_application.py --list --date 2024-03-23
  ```
  
- You can also use `--list DATE` with delete and edit, if you want to see notes for specific dates.

  ```
  python main_application.py --edit --date 2024-03-23
  ```

## Contributing

Contributions to Notes++ are welcome! If you have ideas for new features, bug fixes, or improvements, please open an issue or submit a pull request on GitHub.

