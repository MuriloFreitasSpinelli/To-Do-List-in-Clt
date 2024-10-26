import pickle



current_tasks = {} 
completed_tasks = {}
task_by_id = []

usr_input = ""

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

def sort_ids():
    pass

def remove_task():
    to_del = int(input("Task ID:"))
    key = task_by_id[to_del]
    current_tasks.pop(key)
    print(current_tasks)

def reload():
    load_tasks()

def clear_all():
    global current_tasks
    global completed_tasks
    global task_by_id
    current_tasks = {}
    completed_tasks = {}
    task_by_id = []

def load_tasks():
    global current_tasks
    global completed_tasks
    global task_by_id

    with open('tasks.pkl', 'rb') as f:
        current_tasks = pickle.load(f)
    #with open('completed_tasks.pkl', 'rb') as g:
    #    completed_tasks = pickle.load(g)

def save_tasks():
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(current_tasks, f)

while usr_input != "4":
    print("Hello, welcome to the debug, To-Do")
    print("1: Add Task\n2: Remove Task\n3: Show Tasks\n4: Exit\n5: Custom command\n6:Save\n7:Load")
    usr_input = input()

    if usr_input == "1":
        add_task()

    elif usr_input == "2":
        remove_task()

    elif usr_input == "3":
        task_by_id = list(current_tasks)
        print(task_by_id)
        print(current_tasks)
    elif usr_input == "5":
        usr_input = eval(input("Command:"))
        usr_input()
        print("Command completed")
    elif usr_input == "6":
        save_tasks()
    elif usr_input == "7":
        load_tasks()

