from task_list import TaskList
from task import Task

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
    print(">> l(ist) [c(ompleted)|u(ncompleted)]: Lists all tasks if no argument is given, and completed/uncompleted ones depending on given argument")
    

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
            # To-do: add some logging/error tools for later?
            
        case "r" | "remove":
            id = command[1]
            task_list.remove_task_from_list(id)
            
        case "c" | "complete":
            id = command[1]
            task = task_list.get_task_by_id(id)
            if task is None:
                continue
            task.mark_as_completed()
            
        case "g" | "get":
            id = command[1]
            task = task_list.get_task_by_id(id)
            if task is None:
                continue
            print(task)
            
        case "l" | "list":
            if len(command) == 1:
                task_list.print_tasks()
            elif len(command) == 2:
                match command[2].lower():
                    case "c" | "completed":
                        task_list.print_completed_tasks()
                    case "u" | "uncompleted":
                        task_list.print_uncompleted_tasks()
                    case _:
                        print("[ERROR] Wrong arguments! Check the HELP command for the correct usage")
            else:
                print("[ERROR] Wrong number of arguments!")
                
        case _:
            print("[ERROR] Wrong command! Check the HELP command for the correct usage")
            
        
print("Finalized PROCRASTIONATION LIST!")
print("Sad to see you go... Thanks for using, though... I guess?")
