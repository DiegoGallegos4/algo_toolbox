# Uses python3
import sys


def get_change(m):
    coins = [1, 5, 10]
    change = 0
    for i in range(len(coins), -1, -1):
        while m - coins[i] >= 0:
            m -= coins[i]
            change += coins[i]
    return m


if __name__ == "__main__":
    m = int(input())
    print(get_change(m))
