import os
import argparse
from local_search import ls_run
from bf import brute_force
from approx import approx

parser = argparse.ArgumentParser()

parser.add_argument('-inst', type=str, required=True, help='Input file name')
parser.add_argument('-alg', type=str, choices=['BF', 'Approx', 'LS'], required=True, help='Algorithm type: BF (Brute Force), Approx (Approximation), or LS (Local Search)')
parser.add_argument('-time', type=int, required=True, help='Cutoff time in seconds')
parser.add_argument('-seed', type=int, help='Random seed')


args = parser.parse_args()

print(f"Filename: {args.inst}")
print(f"Algorithm: {args.alg}")
print(f"Time cutoff: {args.time} seconds")

if args.alg == 'BF':
    visited, length = brute_force(args.inst, args.time)

elif args.alg == 'Approx':
    quality, sol = approx(filename= args.inst)

elif args.alg == 'LS':
    best_tour, best_cost = ls_run(args.inst, args.time, args.seed)

#example: python exec.py -inst "Toronto.tsp" -alg "LS" -time 10


