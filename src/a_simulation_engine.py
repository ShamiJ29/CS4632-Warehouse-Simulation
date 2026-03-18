import heapq
import random
import csv
import json
import os
from datetime import datetime

# imports the other modules for warehouse, orders, metrics, and robots
from src.b_warehouse import Warehouse
from src.d_order import Order
from src.e_metrics import MetricsCollector
from src.c_robot import Robot

#Simulation Parameters
SIM_TIME = 480  # total simulation time in minutes
LAMBDA = 10     # average orders per hour
NUM_RUNS = 10   # --- M3 addition: number of runs for multiple scenarios ---
DATA_DIR = "data"  # --- M3 addition: directory to save CSV/JSON data ---

ORDER_ARRIVAL = "ORDER_ARRIVAL" # event type for new order arrivals
ASSIGN_ROBOT = "ASSIGN_ROBOT"   # event type for assigning robots to orders

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

event_queue = []
current_time = 0

def schedule_event(time, event_type, payload=None):
    # Added parameters : time (float): simulation time when the event occurs
    # event_type (str): type of event (e.g., ORDER_ARRIVAL, ASSIGN_ROBOT)
    # payload (optional): additional data needed for the event
    heapq.heappush(event_queue, (time, event_type, payload))

#Order Interarrival Function
def exponential_interarrival():
    #returns : the float in minutes until the next order
    return random.expovariate(LAMBDA / 60)

# single simulation run with CSV/JSON export and logging 
def run_single_simulation(run_id, sim_time=SIM_TIME, lambd=LAMBDA):
    global current_time, event_queue
    current_time = 0
    event_queue = []

    # initialozes warehouse, metrics collector, and robots
    warehouse = Warehouse()
    metrics = MetricsCollector()

    schedule_event(exponential_interarrival(), ORDER_ARRIVAL)

    #logs for time series and events
    time_series = []
    event_log = []

    #runs simulation until either the event queue is empty or simulation time ends 
    while event_queue and current_time < sim_time:
        current_time, event, payload = heapq.heappop(event_queue)

        #record events 
        event_log.append({
            "timestamp": datetime.now().isoformat(),
            "simulation_time": current_time,
            "event": event
        })

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

        # record system state every 5 minutes
        if int(current_time) % 5 == 0:
            time_series.append({
                "simulation_time": current_time,
                "queue_length": len(warehouse.orders),
                "completed_orders": len(metrics.fulfillment_times)
            })

    # export results
    run_prefix = f"run_{run_id:03d}"
    # Time series CSV
    with open(f"{DATA_DIR}/{run_prefix}_timeseries.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["simulation_time","queue_length","completed_orders"])
        writer.writeheader()
        writer.writerows(time_series)
    # Event CSV
    with open(f"{DATA_DIR}/{run_prefix}_events.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp","simulation_time","event"])
        writer.writeheader()
        writer.writerows(event_log)
    # Summary JSON
    summary = {
        "completed_orders": len(metrics.fulfillment_times),
        "average_fulfillment_time": sum(metrics.fulfillment_times)/len(metrics.fulfillment_times) if metrics.fulfillment_times else 0,
        "parameters": {"SIM_TIME": sim_time, "LAMBDA": lambd}
    }
    with open(f"{DATA_DIR}/{run_prefix}_summary.json", "w") as f:
        json.dump(summary, f, indent=4)

    #console output for each run
    print(f"Run {run_id} complete: Orders={summary['completed_orders']}, Avg Time={summary['average_fulfillment_time']:.2f} min")

#run multiple simulations with varied parameters
def run_all_simulations():
    for i in range(1, NUM_RUNS + 1):
        # vary lambda slightly for each run to test different scenarios
        lambd = LAMBDA + (i-1)*2
        run_single_simulation(i, SIM_TIME, lambd)

#this is the entry point
if __name__ == "__main__":
    run_all_simulations()