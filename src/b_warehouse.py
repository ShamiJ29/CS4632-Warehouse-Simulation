from collections import deque
from src.c_robot import Robot
import math

WAREHOUSE_SIZE = 50

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class Warehouse:
    def __init__(self):
        self.orders = deque()
        self.robots = [Robot(i) for i in range(10)]

    def add_order(self, order):
        self.orders.append(order)

    def process_orders(self, current_time):
        completed = []

        for robot in self.robots:
            if robot.available and self.orders:
                order = min(self.orders, key=lambda o: manhattan(robot.position, o.location))
                self.orders.remove(order)

                travel_time = manhattan(robot.position, order.location)
                robot.position = order.location
                robot.available = True

                order.completion_time = current_time + travel_time
                completed.append(order)

        return completed