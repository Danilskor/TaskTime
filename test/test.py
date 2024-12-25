import time
from src.task import Task

task = Task()
task.start_time()
time.sleep(100)
task.stop_timer()
task.get_elapsed_name()