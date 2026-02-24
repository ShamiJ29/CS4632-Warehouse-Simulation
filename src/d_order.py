import random

class Order:
    def __init__(self, arrival_time):

        #initialize a new order in the warehouse

        #parameters : arrival_time : The simulation time when this order arrives

        #attributes : random (x,y) coordinated representing the shelf location of the order
        # (float or None) : time when teh order arrives
        self.arrival_time = arrival_time
        self.location = (random.randint(0, 49), random.randint(0, 49))
        self.completion_time = None
