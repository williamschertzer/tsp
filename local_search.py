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

def simulated_annealing_tsp(locations, max_time, seed, temp=100000, cooling_rate=0.99, k=.8):
    random.seed(seed)
    current_tour = random.sample(range(len(locations)), len(locations))
    print(current_tour)
    current_cost = total_cost(current_tour, locations)
    
    start_time = time.time()
    while time.time() - start_time < max_time:
        new_tour = swap_locations(current_tour)
        new_cost = total_cost(new_tour, locations)

        temp *= cooling_rate

        if new_cost < current_cost or random.uniform(0, 1) < math.exp(-(new_cost - current_cost) / (k * temp)):
            current_tour, current_cost = new_tour, new_cost

    return current_tour, current_cost


# Example usage for multiple cities
folder_path = "DATA"  # Replace with your folder path
cities_locations = {}


# for filename in os.listdir(folder_path):
#     if filename == inst:  # Assuming the files have a .tsp extension
#         city_name = filename.split(".")[0]
#         filepath = os.path.join(folder_path, filename)
#         locations = parse_city_file(filepath)
#         cities_locations[city_name] = locations

def ls_run(inst, time, seed):
    folder_path = "DATA"
    file_path = os.path.join(folder_path,inst)
    city_name = inst.split(".")[0]
    locations = parse_city_file(file_path)
    cities_locations = {}
    cities_locations[city_name] = locations
    best_tour, best_cost = simulated_annealing_tsp(locations, seed = seed, max_time=time)
    print(f"Total Cost in {city_name}:", best_cost)
    return best_tour, best_cost
