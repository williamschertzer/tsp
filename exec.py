import os
import argparse
from local_search import ls_run
from bf import brute_force
from approx import approx

parser = argparse.ArgumentParser()

parser.add_argument('-inst', type=str, required=True, help='Input file name')
parser.add_argument('-alg', type=str, choices=['BF', 'Approx', 'LS'], required=True, help='Algorithm type: BF (Brute Force), Approx (Approximation), or LS (Local Search)')
parser.add_argument('-time', type=int, help='Cutoff time in seconds')
parser.add_argument('-seed', type=int, help='Random seed')


args = parser.parse_args()

# print(f"Filename: {args.inst}")
# print(f"Algorithm: {args.alg}")
# print(f"Time cutoff: {args.time} seconds")

if args.alg == 'BF':
    best_tour, best_cost = brute_force(args.inst, args.time)

elif args.alg == 'Approx':
    best_cost, best_tour = approx(filename= args.inst)

elif args.alg == 'LS':
    best_tour, best_cost = ls_run(args.inst, args.time, args.seed)

filename_parts = []

if args.inst:
    inst = args.inst.split('.tsp')[0]
    filename_parts.append(inst)
if args.alg:
    filename_parts.append(args.alg)
if args.time:
    filename_parts.append(str(args.time))
if args.seed:
    filename_parts.append(str(args.seed))

filename = '_'.join(filename_parts) + '.sol'

with open(filename, 'w') as file:
    file.write(str(best_cost) + '\n')
    best_tour_string = ', '.join(map(str, best_tour))
    file.write(best_tour_string)

#example: python exec.py -inst "Toronto.tsp" -alg "LS" -time 10


