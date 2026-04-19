import argparse
import sys
import os
import json
import time


def main():
    def save_task(task):
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=2)

    def load_tasks():
        if not os.path.exists(TASKS_FILE):
            return []
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    def list_task():
        tasks = load_tasks()
        if len(tasks) == 0:
            print("No task found")
        else:
            for task in tasks:
                status = "x" if task["done"] else " "
                print(f"[{status}] {task['id']} : {task['task']} Due: {task['date']}")

    def main_menu():
        print("Welcome to XTo-DO")
        time.sleep(2)
        print("Your personal task manager")
        time.sleep(1)
        print("This are the list of your task")
        list_task()
    TASKS_FILE ="./task.json"
    main_menu()



    parser =argparse.ArgumentParser()
    parser.add_argument("task",type=str,nargs="?", help="Task to add")
    parser.add_argument("date",type=str,nargs="?", help="date to add")
    parser.add_argument("-l", "--list", help="List all task", action="store_true")
    parser.add_argument("-c", "--complete", type=int, help="Mark a task as complete by ID")
    parser.add_argument("-d" , "--delete", type=int, help="Delete a task by ID")
    args=parser.parse_args()

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)


    if args.list:
        list_task()
        sys.exit(0)
    elif args.task:
        tasks = load_tasks()
        if len(tasks)==0:
            new_id =1
        else:
            new_id = tasks[-1]["id"] +1
        tasks.append({"id": new_id,"task": args.task,"date":args.date,"done":False})
        save_task(tasks)
        print(f"Task {args.task} added with ID of {new_id} the due date {args.date}")

    elif args.complete:
        tasks =load_tasks()
        for task in tasks:
            if task["id"] ==args.complete:
                task["done"] = True
                save_task(tasks)
                print(f"Task {args.complete} marked as complete")
                break

    elif args.delete:
        tasks=load_tasks()
        new_tasks = []
        for task in tasks:
            if task["id"] !=args.delete:
                new_tasks.append(task)
        tasks = new_tasks
        save_task(new_tasks)
        print(f"task with ID of {args.delete} deleted")

if __name__ =="__main__":
    main()

