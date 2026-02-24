import random

class Robot:
    def __init__(self, robot_id):
        #initializes a robot in the warehouse 
        #parameters : robot_id(int): Unique identifier for this robot
        self.robot_id = robot_id
        self.position = (0, 0)
        self.available = True