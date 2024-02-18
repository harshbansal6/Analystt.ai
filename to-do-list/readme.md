# Command-Line Todo List Application

This is a simple command-line to-do list application written in Python. Users can manage their tasks by adding, deleting, marking as completed, searching, and filtering tasks. Each user can have their own to-do list, and tasks are saved to files for persistence.

## Features

- User Authentication: Users can register new accounts or login with existing credentials.
- Task Management: Users can add, delete, and mark tasks as completed.
- Priority and Deadline: Tasks can have priorities (High, Medium, Low) and deadlines.
- Search and Filter: Users can search for tasks based on keywords and filter tasks by priority or deadline.
- Save and Load: Tasks are saved to files for persistence and loaded back when the program starts.

## Usage

1. Run the Python script `todo_list.py`.
2. Choose an option from the menu:
    - Login: Existing users can login with their username and password.
    - Register: New users can register with a username and password.
    - Quit: Exit the application.
3. Once logged in, users can manage their to-do list using various options such as add, delete, mark as completed, display, search, filter, and save tasks.

## Files

- `todo_list.py`: The main Python script containing the implementation of the to-do list application.
- `users.json`: JSON file storing user credentials (username and password).
- `<username>_tasks.json`: JSON files storing tasks for each user.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the LICENSE file for details.

