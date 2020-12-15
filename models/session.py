class Session:

    def __init__(self, name, description, upcoming, capacity, offpeak, id = None):
        self.name = name 
        self.description = description
        self.upcoming = upcoming
        self.capacity = capacity
        self.offpeak = offpeak
        self.id = id