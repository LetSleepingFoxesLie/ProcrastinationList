from task_list import TaskList
from task import Task
from logger import Logger

print("Initialized PROCRASTIONATION LIST!")
print(">> Your usual \"To-do list\", but terrible!")

def get_help() -> None:
    print("[HELP] Available commands:")
    print("- General:")
    print(">> q(uit): Terminates this program")
    print(">> h(elp): Prints this help menu")
    print("- Tasks:")
    print(">> a(dd): Adds a new task to the list")
    print(">> r(emove) <id>: Removes a task by its given ID")
    print(">> c(omplete) <id>: Marks task its given ID as completed")
    print(">> g(et) <id>: Gets the task by its current ID")
    print(">> l(ist) [c(ompleted)|i(ncomplete)]: Lists all tasks if no argument is given, and completed/incomplete ones depending on given argument")
    print(">> s(ave) <file_name>: Saves current list of tasks in a .csv file")
    print(">> f(etch) <file_name>: Loads list of tasks from a .csv file. Alias: load")
    

get_help()

# Initializing list of tasks
task_list = TaskList()

# Main loop
while True:
    
    # Split command into multiple arguments. We can safely split by " " since arguments can't have a whitespace.
    command = input("Command: ").split()

    match command[0].lower():
        
        case "q" | "quit":
            break
        
        case "h" | "help":
            get_help()
            
        case "a" | "add":
            title = input(">> Insert task title: ")
            description = input(">> Insert task description: ")
            
            task_list.add_task_to_list(
                Task(title, description)
            )
            
        case "r" | "remove":
            if len(command) != 2:
                Logger.error("Wrong number of arguments!")
                continue
            id = command[1]
            task_list.remove_task_from_list(id)
            
        case "c" | "complete":
            if len(command) != 2:
                Logger.error("Wrong number of arguments!")
                continue
            id = command[1]
            task = task_list.get_task_by_id(id)
            if task is None:
                continue
            task.mark_as_completed()
            
        case "g" | "get":
            if len(command) != 2:
                Logger.error("Wrong number of arguments!")
                continue
            id = command[1]
            task = task_list.get_task_by_id(id)
            if task is None:
                continue
            print(task)
            
        case "l" | "list":
            if len(command) == 1:
                task_list.print_tasks()
            elif len(command) == 2:
                match command[1].lower():
                    case "c" | "completed":
                        task_list.print_completed_tasks()
                    case "i" | "incomplete":
                        task_list.print_incomplete_tasks()
                    case _:
                        Logger.error("Wrong arguments! Check the HELP command for the correct usage")
            else:
                Logger.error("Wrong number of arguments!")
            
        case "s" | "save":
            if len(command) != 2:
                Logger.error("Wrong number of arguments!")
                continue
            if ".csv" != command[1][-4:] and len(command[1]) <= 5:
                Logger.error("Wrong file format! It must be a .csv")
                continue
            task_list.save_tasks_to_csv(command[1])
            
        case "f" | "fetch" | "load":
            if len(command) != 2:
                Logger.error("Wrong number of arguments!")
                continue
            if ".csv" != command[1][-4:] and len(command[1]) <= 5:
                Logger.error("Wrong file format! It must be a .csv")
                continue
            task_list.load_tasks_from_csv(command[1])
                
        case _:
            Logger.error("Wrong command! Check the HELP command for the correct usage")
            
        
print("Finalized PROCRASTIONATION LIST!")
print("Sad to see you go... Thanks for using, though... I guess?")
