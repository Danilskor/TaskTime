from src.project.check import Check

class CheckList():
    def __init__(self):
        self._check_list = []
        self._description:str = None

    def add_check(self):
        check = Check()
        self._check_list.append(check)

    def delete_check(self, index):
        self._check_list.pop(index)

    @property
    def check_list(self):
        return self._check_list
    
    def __call__(self):
        return self._check_list
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description