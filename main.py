import time
import datetime
from src.project.task import Task

task = Task()
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(1, 0, 0)
task.task_start_time = start_time
task.task_end_time = end_time

task.add_check_list()
task.check_list.add_check()

task.check_list.description = "Check List Test"
task.check_list.check_list[0].description = "Check Test"
print(task.check_list.description)
print(task.check_list.check_list[0].description)