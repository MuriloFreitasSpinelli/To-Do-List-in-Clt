import pickle



current_tasks = {} 
completed_tasks = {}
task_by_id = []

usr = ""

current_id = 0

def make_id():
    global current_id
    current_id = current_id + 1
    return current_id

def add_task():
    title = input("Titel:")
    description = input("Description:")
    project = input("Project:")

    task_id = make_id()
    current_tasks[task_id] = {"Titel": title, "Description": description, "Project": project}


def remove_task():
    to_go = int(input("Task ID:"))
    key = task_by_id[to_go]
    current_tasks.pop(key)
    print(current_tasks)


def load_tasks():
    pass

def save_tasks():
    pass

while usr != "4":
    print("Hello, welcome to the debug, To-Do")
    print("1: Add Task\n2: Remove Task\n3: Show Tasks\n4: Exit")
    usr = input()

    if usr == "1":
        add_task()


    elif usr == "2":
        remove_task()

    elif usr == "3":
        task_by_id = list(current_tasks)
        print(task_by_id)
        print(current_tasks)



