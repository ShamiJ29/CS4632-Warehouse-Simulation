# CS4632-Warehouse-Simulation

# Warehouse Operations Simulation

## Course
CS 4632 – Modeling and Simulation

## Author
Shamitha John

## Project Description
This project simulates warehouse operations including order processing,
inventory management, and robot-assisted picking and delivery.

The goal is to analyze order fulfillment time, robot utilization,
and storage efficiency under order arrivals.

## Features
Poisson-based random order generation
Discrete-event simulation engine
Robot assignment using Manhattan distance
Advanced routing (distance + queue-based prioritization)
Inventory tracking with restocking policy
Multi-run simulation execution (10+ runs)
Automated data collection
Export of results to CVS and JSON
Event logging time stamps


## Technology
Language: Python 
Simulation Type: Discrete-Event Simulation

## Repository Structure
/src        -> Simulation source code  
/docs       -> Reports and documentation 
/data       -> Output data (CSV/JSON) 


---

## Implementation Status (M3 Complete)

### Completed Features
- Poisson order arrival model
- Full event-driven simulation engine
- Robot assignment and routing logic
- Inventory management with restocking
- Performance metrics tracking
- Multi-run simulation with parameter variation
- Data export (time-series, event logs, summary statistics)


## Simulation Parameters
The simulation allows variation of:
- Order arrival rate (LAMBDA)
- Simulation duration (SIM_TIME)
- Number of robots
- Randomized order locations


## Data Collection
The simulation collects:

### Time-Series Data
- Queue length over time
- Completed orders

### Event Data
- Event type (ORDER_ARRIVAL, ASSIGN_ROBOT)
- Simulation timestamp
- Real-world timestamp

### Summary Statistics
- Total completed orders
- Average fulfillment time
- Simulation parameters

All data is exported in structured formats:
- CSV (time-series, events)
- JSON (summary)


## Installation Instructions

### Requirements
- Python 3.8+
- No external libraries required

### Setup 
bash : git clone https://github.com/ShamiJ29/CS4632-Warehouse-Simulation.git
cd CS4632-Warehouse-Simulation

Run the Simulation : python3 -m src.a_simulation_engine

This should be all the correct files : 
a_simulation_engine.py  
b_warehouse.py  
c_robot.py  
d_order.py  
e_metrics.py  
__init__.py

Expected output should be the total orders completed, average fulfillment time per run and CSV and JSON data files generated in /data


## Architectural Overview
- a_simulation_engine.py - handles event scheduling and simulation execution
- b_warehouse.py - manages order queue, robots, and inventory
- c_robot.py - represents robot behavior and state
- d_order.py - defines order attributes and lifecycle
- e_metrics.py - collects performance metrics

## UML Design : 
- SimulationEngine --> a_simulation_engine.py
- Warehouse --> b_warehouse.py
- Robot --> c_robot.py
- Order --> d_order.py
- MetricsCollector --> e_metrics.py

## Changes from M3
- Enhanced routing logic to include queue-aware prioritization
- Added full data collection and export system

Conclusion notes : This M3 project demonstrates the complete implementation of the features and also sumtiple simulation runs with varied parameters. It also has a comprehensive data collection and a structures output for analysis. 
