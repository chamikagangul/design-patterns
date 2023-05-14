import copy

class ConcretePrototype:
    name = None
    value = None
    
    def __init__(self):
        self.name = ""
        self.value = 0

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)