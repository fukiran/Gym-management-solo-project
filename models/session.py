class Session:

    def __init__(self, name, description, upcoming, capacity, id = None):
        self.name = name 
        self.description = description
        self.upcoming = upcoming
        self.capacity = capacity
        self.id = id