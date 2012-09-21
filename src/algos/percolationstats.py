"""
Calculates the Percolation ratio using Union algoritm

Example usage:
python percolationstats.py -n 200 -t 20
"""
import argparse
import random

from percolation import Percolation

parser = argparse.ArgumentParser(description='Calculate the percolation ratio')
parser.add_argument('-n', action='store', dest='n', type=int,
                    help='The grid size n * n')
parser.add_argument('-t', action='store', dest='t', type=int,
                    help='How often should the experiment be executed.')


results = parser.parse_args()
n = results.n
t = results.t

percolation_results = []
for i in range(0, results.t):
    perc = Percolation(n)
    open_sites = 0
    while not perc.percolates():
        row = random.randint(1, n)
        column = random.randint(1, n)
        if not perc.is_open(row, column):
            perc.open(row, column)
            open_sites += 1
    percolation = (open_sites * 1.0) / (n * n)
    print percolation
    percolation_results.append(percolation)

mean = sum(percolation_results) / len(percolation_results)
print "Mean: ", mean