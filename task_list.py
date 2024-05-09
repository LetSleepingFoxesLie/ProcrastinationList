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
            if t.is_completed:
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
        for t in self.tasks:
            if t.task_id == id:
                Logger.log(f"Found task with id {id}!")
                return t
        print(f"[ERROR] Task with ID {id} has not been found!")
        return None