from collections import deque
from src.c_robot import Robot
import math

# Warehouse Parameters
WAREHOUSE_SIZE = 50

def manhattan(a, b):
    # parameters: a (tuple), b (tuple)
    # returns: Manhattan distance between points a and b
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class Warehouse:
    def __init__(self):
        # Initializes the warehouse instance
        # attributes: orders, robots
        self.orders = deque()
        self.robots = [Robot(i) for i in range(10)]

        # added in Inventory System 
        self.inventory = {(x, y): 5 for x in range(50) for y in range(50)}
        self.restock_threshold = 2
        self.restock_amount = 5

        # Queue Tracking
        self.queue_lengths = []

    def add_order(self, order):
        # Add a new order to the warehouse queue
        self.orders.append(order)

    def process_orders(self, current_time):
        # parameters: current_time (float) : simulation time
        # returns: orders that have been finished
        completed = []

        # Track queue length 
        self.queue_lengths.append(len(self.orders))

        for robot in self.robots:
            # Only assign order to robots that are available
            if robot.available and self.orders:

                # Advanced Robot Routing & Inventory Check 
                order = min(
                    self.orders,
                    key=lambda o: manhattan(robot.position, o.location) + len(self.orders) * 0.1
                )

                if self.inventory[order.location] <= 0:
                    continue  # skip if out of stock

                # Remove the selected order from the queue
                self.orders.remove(order)

                # Compute travel time based on Manhattan distance
                travel_time = manhattan(robot.position, order.location)

                #Robot Utilization Tracking 
                if hasattr(robot, "busy_time"):
                    robot.busy_time += travel_time

                # Update robot position
                robot.position = order.location
                robot.available = True

                # added in Inventory System 
                self.inventory[order.location] -= 1
                if self.inventory[order.location] <= self.restock_threshold:
                    self.inventory[order.location] += self.restock_amount

                # Record order completion time
                order.completion_time = current_time + travel_time
                completed.append(order)

        return completed