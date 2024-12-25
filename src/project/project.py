from src.project.task import Task
from src.project.description import Description

class Project(Description):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)

    def set_name(self, name):
        self._name = name
    

