# uses local search algorithm based on simulated annealing to find the find a path and with low cost
# the main function ls_run locates the specified data file and passees it through the simulated_annealing_tsp function along
# with the arguments for time and seed. A random initial tour is generated using the provided seed. The cost of that initial
# tour is calculated with the total_cost function which calcualtes the cost between locations using the calculate_distance function
# then, random swaps occur and the new cost is calculated. The new tour is accepted if the new cost is lower or if it is higher cost 
# but with some probability based on a temperature that is decreasing throughout the simulation, and a constant K.

import pandas as pd
import numpy as np
import os
import math
import random
import time

def parse_city_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    locations = []
    for line in lines:
        if line.strip() == "NODE_COORD_SECTION":
            continue
        elif line.strip() == "EOF":
            break
        else:
            parts = line.split()
            if len(parts) == 3:
                _, x, y = parts
                locations.append((float(x), float(y)))

    return locations

def calculate_distance(point1, point2):
    return round(math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2))

def total_cost(tour, locations):
    cost = 0
    for i in range(len(tour)):
        cost += calculate_distance(locations[tour[i-1]], locations[tour[i]])
    return cost

def swap_locations(tour):
    tour = tour.copy()
    i, j = random.sample(range(len(tour)), 2)
    tour[i], tour[j] = tour[j], tour[i]
    return tour

def simulated_annealing_tsp(locations, max_time, seed= 0, temp=100000, cooling_rate=0.99, k=.8):
    random.seed(seed)
    current_tour = random.sample(range(len(locations)), len(locations))
    current_cost = total_cost(current_tour, locations)
    
    start_time = time.time()
    while time.time() - start_time < max_time:
        new_tour = swap_locations(current_tour)
        new_cost = total_cost(new_tour, locations)

        temp *= cooling_rate

        if new_cost < current_cost or random.uniform(0, 1) < math.exp(-(new_cost - current_cost) / (k * temp)):
            current_tour, current_cost = new_tour, new_cost

    return current_tour, current_cost

def ls_run(inst, time, seed):
    folder_path = "DATA"
    file_path = os.path.join(folder_path,inst)
    city_name = inst.split(".")[0]
    locations = parse_city_file(file_path)
    cities_locations = {}
    cities_locations[city_name] = locations
    best_tour, best_cost = simulated_annealing_tsp(locations, seed = seed, max_time=time)
    return best_tour, best_cost
