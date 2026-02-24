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
and storage efficiency under stochastic order arrivals.

## Features
Random order generation
Inventory tracking
Robot routing
Performance metrics collection
Discrete-event simulation model

## Technology
Language: Python 
Simulation Type: Discrete-Event Simulation

## Repository Structure
/src        -> Simulation source code  
/docs       -> Project reports and UML diagrams  
/data       -> Input/output datasets  

## Project Status
Implemented so far : 
- Poisson order arrivals
- Discrete-event simulation
- robot assignment (manhattan distance)
- Performance metrics collection
- Entities : Warehouse, Robot, Order, Metrics

## In Progress 
- inventory restocking logic (trigger restock when it's below the threshold )

## TO do 
- Advanced robot routing
- GUI or enhanced output visualization

## Changes from Original Proposal 
- Refactores source files with prefixes so the files will stay in the correct order
## Installation Instructions

  ## Requirements : Python 3.8+, and no external packages are required

### Setup
- clone this : git clone https://github.com/ShamiJ29/CS4632-Warehouse-Simulation.git

- navigate to the folder : cd CS4632-Warehouse-Simulation

This should be all the correct files : a_simulation_engine.py  
b_warehouse.py  
c_robot.py  
d_order.py  
e_metrics.py  
__init__.py


Expected output should be the total orders completed and the average fulfillment time. 

## Architectural Overview
- a_simulation_engine.py - simulation engine and event scheduler
- b_warehouse.py - warehouse class, manages order queue and robot assignments
- c_robot.py - robot entity, tracks position and availabiliy
- d_order.py - order entity, tracks arrival, location and completion time
- e_metrics.py - collects performance metrics

## UML Design : 
- SimulationEngine --> a_simulation_engine.py
- Warehouse --> b_warehouse.py
- Robot --> c_robot.py
- Order --> d_order.py
- MetricsCollector --> e_metrics.py
