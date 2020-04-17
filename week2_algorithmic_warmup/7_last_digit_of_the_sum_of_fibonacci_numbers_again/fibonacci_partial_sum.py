# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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


def fibonacci_partial_sum(m, n):
    return (get_fibonacci_huge(n + 2, 10) - get_fibonacci_huge(m + 1, 10)) % 10


if __name__ == "__main__":
    inp = input()
    from_, to = map(int, inp.split())
    print(fibonacci_partial_sum(from_, to))
