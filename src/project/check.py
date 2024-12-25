from src.project.description import Description

class Check(Description):
    def __init__(self):
        super().__init__()
        self._description:str = None
        self._is_check:bool = False
    
    def check(self):
        self._is_check = True
    
    def uncheck(self):
        self._is_check = False

    @property
    def check(self):
        return self._is_check
    