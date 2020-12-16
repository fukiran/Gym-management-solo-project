class Member:
    
    def __init__(self, name, age, premium, active, id = None):
        self.name = name 
        self.age = age 
        self.premium = premium
        self.active = active
        self.id = id 

    def __eq__(self, other):
        if self.id == other.id:
            return True
        return False 