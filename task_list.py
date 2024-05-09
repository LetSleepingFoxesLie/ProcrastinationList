from task import Task

class TaskList:
    def __init__(self):
        self.tasks = list()
    
    def add_task_to_list(self, task: Task) -> None:
        self.tasks.append(task)
    
    def remove_task_from_list(self, task: Task, id: int) -> None:
        for t in self.tasks:
            if t.task_id == id:
                self.tasks.remove(t)
                return
        else:
            return
    
    def print_tasks(self) -> None:
        for t in self.tasks:
            print(t)
    
    def print_uncompleted_tasks(self) -> None:
        for t in self.tasks:
            if not t.is_completed:
                print(t)
    
    def print_completed_tasks(self) -> None:
        for t in self.tasks:
            if t.is_completed:
                print(t)

    def get_task_by_id(self, id: int) -> Task:
        for t in self.tasks:
            if t.task_id == id:
                print(f"[LOG] Task with ID {id} was successfully found.")
                return t
        print(f"[ERROR] Task with ID {id} has not been found!")
        return None