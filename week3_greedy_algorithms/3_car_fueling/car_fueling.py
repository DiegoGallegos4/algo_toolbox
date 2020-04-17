# python3
import sys


def compute_min_refills(distance, tank, stops):
    current_distance = 0
    min_num_refills, current_stop = 0, 0
    while current_distance < d and current_stop <= len(stops):
        next_refill = current_stop + 1
        while m >= stops[next_refill] - stops[current_stop] and next_refill < len(stops):
            next_refill += 1
        min_num_refills += 1
        current_stop = next_refill - 1
    return min_num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
