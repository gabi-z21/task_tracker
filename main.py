import json
import os
import sys 
""" this is a mini project to make a task tracker that can add, update, save, load 
and delete tasks """
class TaskTracker:
    def __init__(self, file_name = "tasks.json"):
        self.file_name = file_name
        self.tasks = []
        self.load_tasks() #load tasks from files when object is created

    def load_tasks(self):
        try:
            if os.path.exists(self.file_name): #check if file exists
               with open(self.file_name, "r") as file:
                  self.tasks = json.load(file)
        except json.JSONDecodeError: # if file is not found or any other error occurs, start with empty list
            self.tasks = []


    def save_tasks(self):
        with open(self.file_name , "w") as file:
            json.dump(self.tasks, file, indent = 4) # save tasks to file 
            print("tasks saved successfully!")
#add task to file
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False}) 
        self.save_tasks()
        print(f"Task '{task}' added successfully!")
#delete task from file
    def delete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                self.save_tasks()
                print(f"Task deleted: {t['task']}")
                return
        print("task not found")
#update an already existing task
    def update_task(self, old_task, new_task):
        for t in self.tasks:
            if t["task"] == old_task:
               t["task"] = new_task
               self.save_tasks()
               print(f"Task updated to '{new_task}'.")
               return
           
        print("the task you entered was not found")
    
#view all tasks in the file
    def list_tasks(self):
        if self.tasks:
            for i , task in enumerate(self.tasks, start = 1):
               status = "✔"  if task["completed"] else "❌"
               print(f"{i}. {task['task']} [{status}]")
        else:
            print("No tasks found.")

#CLI file handling
if len(sys.argv) < 2:
    print("Usage: python main.py [add|delete|update|list] ...")
    sys.exit()

command = sys.argv[1].lower()
tracker = TaskTracker()

if command == "add" and len(sys.argv) >= 3:
    tracker.add_task(" ".join(sys.argv[2:]))
elif command == "delete" and len(sys.argv) >= 3:
    tracker.delete_task(" ".join(sys.argv[2:]))
elif command == "update" and len(sys.argv) >= 4:
    tracker.update_task(sys.argv[2], " ".join(sys.argv[3:]))
elif command == "list":
    tracker.list_tasks()
else:
    print("Invalid command or missing arguments.")


