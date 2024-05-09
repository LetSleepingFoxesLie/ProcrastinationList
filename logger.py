class Logger():
    def __init__(self):
        #self.show_logs: True
        #self.show_warns: True
        #self.show_errors: True
        pass
    
    def log(text):
        print(f"[LOG] {text}")
        
    def warn(text):
        print(f"[WARN] {text}")
        
    def error(text):
        print(f"[ERROR] {text}")