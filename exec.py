import os
import argparse
from local_search import simulated_annealing_tsp

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
  #call bf file

elif args.alg == 'Approx':
  #call approx file

else args.alg == 'LS':
  simulated_annealing_tsp(args.time, args.seed)

#example: python exec.py -inst "ghl.txt" -alg "BF" -time 100

