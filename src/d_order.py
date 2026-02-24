import random

class Order:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        self.location = (random.randint(0, 49), random.randint(0, 49))
        self.completion_time = None
