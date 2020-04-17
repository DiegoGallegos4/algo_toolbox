# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.0
    items = sorted(zip(weights, values), key=lambda elt: elt[1] / elt[0], reverse=True)
    for (w, v) in items:
        if capacity == 0:
            break
        weight_to_take = min(w, capacity)
        value += weight_to_take * v / w
        capacity -= weight_to_take
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
