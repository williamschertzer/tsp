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

print(f"Filename: {args.inst}")
print(f"Algorithm: {args.alg}")
print(f"Time cutoff: {args.time} seconds")

if args.alg == 'BF':
    best_tour, best_cost = brute_force(args.inst, args.time)

elif args.alg == 'Approx':
    best_cost, best_tour = approx(filename= args.inst)

elif args.alg == 'LS':
    best_tour, best_cost = ls_run(args.inst, args.time, args.seed)


with open(f'{args.inst}_{args.alg}_{args.time}_{args.seed}.sol', 'w') as file:
    file.write(f'Length: {best_cost}')
    file.write(f'Vertex_IDs: {best_tour}')
#example: python exec.py -inst "Toronto.tsp" -alg "LS" -time 10


