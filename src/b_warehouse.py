from collections import deque
from src.c_robot import Robot
import math

#Warehouse Parameters
WAREHOUSE_SIZE = 50

def manhattan(a, b):

    #parameters : a (tuple): (x, y) coordinates of the first point
    # b (tuple): (x, y) coordinates of the second point
    #returns : the Manhattan distance between points a and b
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class Warehouse:
    def __init__(self):
        # Initializes the warehouse instance 
        #attributes : order : Queue of pending orders
        #robots : list of robot objects available to process orders
        self.orders = deque()
        self.robots = [Robot(i) for i in range(10)]

    def add_order(self, order):

        #add a new order to the warehouse queue
        #parameters : order object to be added
        self.orders.append(order)

    def process_orders(self, current_time):
        #parameters : current_time (float) : simulation time

        #returns : orders that have been finihsed
        completed = []

        for robot in self.robots:
            #only assign order to robots that are available 
            if robot.available and self.orders:
                order = min(self.orders, key=lambda o: manhattan(robot.position, o.location))
                #Remove the seleected from the queue
                self.orders.remove(order)
#Compute travel time based on Manhattan distance
                travel_time = manhattan(robot.position, order.location)
                robot.position = order.location
                robot.available = True
#Record order completion time
                order.completion_time = current_time + travel_time
                completed.append(order)

        return completed