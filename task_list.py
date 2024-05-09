from task import Task
from logger import Logger

class TaskList:
    def __init__(self):
        self.tasks = list()
    
    def add_task_to_list(self, task: Task) -> None:
        
        Logger.log(f"Added task \"{task.title}\" (ID: {task.task_id}) to list.")
        self.tasks.append(task)
    
    def remove_task_from_list(self, id: int) -> None:
        task = self.get_task_by_id(id)
        if task is None:
            return
        Logger.log(f"Removed task \"{task.title}\" (ID: {task.task_id}) from list.")
        self.tasks.remove(task)
        
    def print_tasks(self) -> None:
        if len(self.tasks) == 0:
            Logger.log("List of tasks is empty!")
            return
        for t in self.tasks:
            print(t)
    
    def print_incomplete_tasks(self) -> None:
        if len(self.tasks) == 0:
            Logger.log("List of tasks is empty!")
            return
        
        incomplete_tasks = list()
        for t in self.tasks:
            if not t.is_completed:
                incomplete_tasks.append(t)
                
        if len(incomplete_tasks) == 0:
            Logger.log("List of incomplete tasks is empty!")
            return
        else:
            for t in incomplete_tasks:
                print(t)
    
    def print_completed_tasks(self) -> None:
        if len(self.tasks) == 0:
            Logger.log("List of tasks is empty!")
            return
        
        completed_tasks = list()
        for t in self.tasks:
            if t.is_completed:
                completed_tasks.append(t)
                
        if len(completed_tasks) == 0:
            Logger.log("List of completed tasks is empty!")
            return
        else:
            for t in completed_tasks:
                print(t)

    def get_task_by_id(self, id: int) -> Task:
        try:
            id = int(id)
        except ValueError:
            Logger.error("ID must be a number!")
            return
        
        for t in self.tasks:
            if t.task_id == id:
                Logger.log(f"Found task with id {id}!")
                return t
        print(f"[ERROR] Task with ID {id} has not been found!")
        return None
    
    def save_tasks_to_csv(self, file_name: str) -> None:
        if len(self.tasks) == 0:
            Logger.error("List of tasks is empty! Cannot continue.")
            return

        try:
            with open(file_name, "w") as f:
                f.write(f"Title,Description,Is completed?\n") # ID is irrelevant
                for task in self.tasks:
                    f.write(f"{task.title},{task.description},{task.is_completed}\n")
                Logger.log(f"Saved tasks to file {file_name}")
        except FileExistsError:
            Logger.error("File name already exists!")
        finally:
            return
        
    def load_tasks_from_csv(self, file_name: str) -> None:
        # I know I should be using the csv library, but this project is so barebones I don't feel the need...
        try:
            with open(file_name, "r") as f:
                lines = f.readlines()[1:] # Pruning the first line since it's technically useless for our purposes
                
                # Wipe current task list
                self.tasks = list()
                Task.counter = 0
                
                # Generating tasks from each line
                for line in lines:
                    arguments = line.split(",")
                    self.add_task_to_list(
                        Task(
                            title = arguments[0], 
                            description = arguments[1],
                            completed = arguments[2]
                        )
                    )
                    
                Logger.log(f"Loaded tasks from file {file_name}")
        except FileNotFoundError:
            Logger.error("File not found! Make sure you entered the correct file name.")
        finally:
            return