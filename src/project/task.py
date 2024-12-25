from src.project.timer import Timer
from src.project.check_list import CheckList
from src.project.description import Description
import datetime

class Task(Description):
    def __init__(self):
        super().__init__()
        self._max_time = None
        self._check_list = None
        self._timer = Timer()
    
    def start_time(self):
        self._timer.start_timer()
    
    def stop_timer(self):
        self._timer.stop_timer()
    
    def get_elapsed_name(self):
        return self._timer.get_elapsed_time()
    
    @property
    def task_start_time(self):
        return self._task_start_time
    
    @task_start_time.setter
    def task_start_time(self, task_start_time: datetime.datetime):
        self._task_start_time = task_start_time

    @property
    def task_end_time(self):
        return self._task_stop_time

    @task_end_time.setter
    def task_end_time(self, task_stop_time: datetime.datetime):
        self._task_stop_time = task_stop_time

    def add_check_list(self):
        self._check_list = CheckList()
    
    @property
    def check_list(self):
        return self._check_list

    
