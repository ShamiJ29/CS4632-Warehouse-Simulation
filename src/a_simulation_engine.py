import heapq
import random
# imports the other modules for warehouse, orders, metrics, and robots
from src.b_warehouse import Warehouse
from src.d_order import Order
from src.e_metrics import MetricsCollector
from src.c_robot import Robot

#Simulation Parameters

SIM_TIME = 480  # total simulation time in minutes
LAMBDA = 10     # average orders per hour

ORDER_ARRIVAL = "ORDER_ARRIVAL" # event type for new order arrivals
ASSIGN_ROBOT = "ASSIGN_ROBOT" # event type for assigning robots to orders

event_queue = []
current_time = 0

def schedule_event(time, event_type, payload=None):
    # Added parameters : time (float): simulation time when the event occurs
    # event_type (str): type of event (e.g., ORDER_ARRIVAL, ASSIGN_ROBOT)
    # payload (optional): additional data needed for the event
    heapq.heappush(event_queue, (time, event_type, payload))

#Order Interarrival Function
def exponential_interarrival():
    return random.expovariate(LAMBDA / 60)

#returns : the float in minutes until the next order

#Main simulation loop
def run():
    global current_time

# initialozes warehouse, metriscs, collecotor, and robots
    warehouse = Warehouse()
    metrics = MetricsCollector()

    schedule_event(exponential_interarrival(), ORDER_ARRIVAL)

#runs simulation until either teh event queue is empty or simulation time ends 
    while event_queue and current_time < SIM_TIME:
        current_time, event, payload = heapq.heappop(event_queue)

#Handles Order Arrival Events
        if event == ORDER_ARRIVAL:
            order = Order(current_time)
            warehouse.add_order(order)
            schedule_event(current_time + exponential_interarrival(), ORDER_ARRIVAL)
            schedule_event(current_time, ASSIGN_ROBOT)

#Handles Robot Assignment Events
        elif event == ASSIGN_ROBOT:
            completed_orders = warehouse.process_orders(current_time)
            for o in completed_orders:
                metrics.record_order(o, current_time)

    metrics.report()
#this is the entry point
if __name__ == "__main__":
    run()