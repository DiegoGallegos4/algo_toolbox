# Uses python3
import sys


def optimal_summands(n):
    summands = []
    left, right = 1, n
    while right > 0:
        if left < right / 2:
            summands.append(left)
            right -= left
            left += 1
        else:
            summands.append(right)
            right = 0
    return summands


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=" ")
