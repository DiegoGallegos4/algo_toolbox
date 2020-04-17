# Uses python3
def calc_fib_naive(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


n = int(input())
print(calc_fib(n))
