# python3


def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


# 2n comparisons
def max_pairwise_product_fast(numbers):
    index = 0
    n = len(numbers)
    for i in range(1, n):
        if numbers[i] > numbers[index]:
            index = i
    numbers[index], numbers[n - 1] = numbers[n - 1], numbers[index]
    index = 0
    for i in range(1, n - 1):
        if numbers[i] > numbers[index]:
            index = i
    numbers[index], numbers[n - 2] = numbers[n - 2], numbers[index]
    return numbers[n - 1] * numbers[n - 2]


# ~1.5 comparisons
def max_pairwise_product(numbers):
    largest, second = 0, 1
    if numbers[largest] < numbers[second]:
        largest, second = 1, 0

    for i in range(2, len(numbers)):
        if numbers[largest] < numbers[i]:
            numbers[second] = numbers[largest]
            largest = i
        elif numbers[second] < numbers[i]:
            second = i
    return numbers[largest] * numbers[second]


def stress_test(n, m):
    import random

    input_len = random.randint(2, n)
    arr = [0] * input_len
    for i in range(input_len):
        arr[i] = random.randint(0, m)
    naive = max_pairwise_product_naive(arr)
    fast = max_pairwise_product(arr)
    if naive == fast:
        print("OK")
    else:
        print("Wrong answer: ", naive, fast)
        return


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
    # for n, m in [(10, 100), (100, 1000), (1000, 10000)]:
    #     stress_test(n, m)
