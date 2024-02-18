import json
import os
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority=None, deadline=None):
        self.tasks.append({
            "task": task,
            "priority": priority,
            "deadline": deadline,
            "completed": False
        })

    def delete_task(self, index):
        del self.tasks[index]

    def mark_task_completed(self, index):
        self.tasks[index]["completed"] = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = " [x] " if task["completed"] else " [ ] "
                priority = f"Priority: {task['priority']} | " if task["priority"] else ""
                deadline = f"Deadline: {task['deadline']} | " if task["deadline"] else ""
                print(f"{i + 1}. {status}{task['task']} | {priority}{deadline}")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.tasks = json.load(file)

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task["task"].lower()]

    def filter_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task["priority"] == priority]

    def filter_tasks_by_deadline(self, deadline):
        return [task for task in self.tasks if task["deadline"] == deadline]


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.todo_list = TodoList()

    def authenticate(self, password):
        return self.password == password


def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            return {user_data["username"]: User(user_data["username"], user_data["password"]) for user_data in json.load(file)}
    return {}


def save_users(users):
    with open("users.json", "w") as file:
        json.dump([{"username": user.username, "password": user.password} for user in users.values()], file)


def main():
    users = load_users()

    while True:
        print("\nTodo List Options:")
        print("1. Login")
        print("2. Register")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            user = users.get(username)
            if user and user.authenticate(password):
                print("Login successful!")
                todo_list = user.todo_list
                while True:
                    print("\nTodo List Options:")
                    print("1. Add Task")
                    print("2. Delete Task")
                    print("3. Mark Task as Completed")
                    print("4. Display Tasks")
                    print("5. Search Tasks")
                    print("6. Filter Tasks by Priority")
                    print("7. Filter Tasks by Deadline")
                    print("8. Save Tasks to File")
                    print("9. Logout")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        task = input("Enter task to add: ")
                        priority = input("Enter priority (High, Medium, Low): ")
                        deadline = input("Enter deadline (YYYY-MM-DD): ")
                        todo_list.add_task(task, priority, deadline)
                        print("Task added successfully.")

                    elif choice == "2":
                        index = int(input("Enter index of task to delete: ")) - 1
                        if 0 <= index < len(todo_list.tasks):
                            todo_list.delete_task(index)
                            print("Task deleted successfully.")
                        else:
                            print("Invalid index.")

                    elif choice == "3":
                        index = int(input("Enter index of task to mark as completed: ")) - 1
                        if 0 <= index < len(todo_list.tasks):
                            todo_list.mark_task_completed(index)
                            print("Task marked as completed.")
                        else:
                            print("Invalid index.")

                    elif choice == "4":
                        print("\nTasks:")
                        todo_list.display_tasks()

                    elif choice == "5":
                        keyword = input("Enter keyword to search: ")
                        results = todo_list.search_tasks(keyword)
                        print("\nSearch Results:")
                        for i, task in enumerate(results):
                            print(f"{i + 1}. {task['task']}")

                    elif choice == "6":
                        priority = input("Enter priority to filter (High, Medium, Low): ")
                        filtered_tasks = todo_list.filter_tasks_by_priority(priority)
                        print("\nFiltered Tasks by Priority:")
                        for i, task in enumerate(filtered_tasks):
                            print(f"{i + 1}. {task['task']}")

                    elif choice == "7":
                        deadline = input("Enter deadline to filter (YYYY-MM-DD): ")
                        filtered_tasks = todo_list.filter_tasks_by_deadline(deadline)
                        print("\nFiltered Tasks by Deadline:")
                        for i, task in enumerate(filtered_tasks):
                            print(f"{i + 1}. {task['task']}")

                    elif choice == "8":
                        todo_list.save_to_file(f"{username}_tasks.json")
                        print("Tasks saved to file.")

                    elif choice == "9":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid username or password.")

        elif choice == "2":
            username = input("Enter a new username: ")
            if username in users:
                print("Username already exists. Please choose another.")
                continue
            password = input("Enter a new password: ")
            users[username] = User(username, password)
            save_users(users)
            print("User registered successfully.")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

