class Description:
    def __init__(self):
        self._description:str = None

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = str(description)