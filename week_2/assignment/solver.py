#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List
from item import Item
from dynamic_programming import dynamic_programming_naive


def greedy(items: List, capacity: int):
    value = 0
    weight = 0
    taken = [0] * len(items)
    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    return value, taken


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()

    # nr of items in existence
    item_count = int(firstLine[0])

    # capacity of the knapsack
    capacity = int(firstLine[1])

    # parse items info
    items = []
    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full

    # value, taken = greedy(items, capacity)
    value, taken = dynamic_programming_naive(items=items, capacity=capacity)
    # value, taken = branch_and_bound(items=items, capacity=capacity, value_max=0, value_acc=0, items_selected=[])

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(2000)

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
