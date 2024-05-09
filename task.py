class Task:
    
    counter = 0
    
    def __init__(self, title, description):
        self.task_id = Task.counter
        self.title = title
        self.description = description
        self.is_completed = False
        
        Task.counter += 1
    
    def mark_as_completed(self):
        if not self.is_completed:
            self.is_completed = True
        else:
            return
    
    def was_completed(self):
        return "Yes" if self.is_completed else "No"
    
    def __str__(self):
        s = str()
        s += f"[Task ID: {self.task_id}] {self.title}\n"
        s += f">> {self.description}\n"
        s += f">> Completed? {self.was_completed()}\n"
        return s