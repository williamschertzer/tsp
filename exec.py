import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-inst', type=str, required=True, help='Input file name')
parser.add_argument('-alg', type=str, choices=['BF', 'Approx', 'LS'], required=True, help='Algorithm type: BF (Brute Force), Approx (Approximation), or LS (Local Search)')
parser.add_argument('-time', type=int, required=True, help='Cutoff time in seconds')
parser.add_argument('-seed', type=int, help='Random seed')


args = parser.parse_args()

print(f"Filename: {args.inst}")
print(f"Algorithm: {args.alg}")
print(f"Time cutoff: {args.time} seconds")

#example: python exec.py -inst "ghl.txt" -alg "BF" -time 100
