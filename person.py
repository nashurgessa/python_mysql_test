
class Person:
    def __init__(self, 
                 name=None, 
                 id=None, 
                 mother=None, 
                 father=None):
        self.name = name
        self.id = id
        self.mother = mother
        self.father = father
        
    def get_name(self):
        return self.name
    def  set_name(self, name):
        self.name = name;
    def get_id(self):
        return self.id
    def get_mother(self):
        return self.mother
    def get_father(self):
        return self.father
    
    