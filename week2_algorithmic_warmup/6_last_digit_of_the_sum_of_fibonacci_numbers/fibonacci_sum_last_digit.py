# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def get_fibonacci_huge(n, m):
    def get_pisano(m):
        prev, curr = 0, 1
        for i in range(0, m * m):
            prev, curr = curr, (prev + curr) % m
            if prev == 0 and curr == 1:
                return i + 1

    pisano = get_pisano(m)
    n = n % pisano

    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr % m


def fibonacci_sum(n):
    return get_fibonacci_huge(n + 2, 10) - 1


if __name__ == "__main__":
    inp = input()
    n = int(inp)
    print(fibonacci_sum(n))
