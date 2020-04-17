# Uses python3

import sys


def is_greater_or_equal(a, b):
    if a + b > b + a:
        return True
    else:
        return False


def largest_number(a):
    ans = ""
    while a:
        max_digit = None
        max_digit_idx = 0
        for i in range(len(a)):
            if not max_digit:
                max_digit = a[i]
            if is_greater_or_equal(a[i], max_digit):
                max_digit = a[i]
                max_digit_idx = i
        ans += max_digit
        a.pop(max_digit_idx)
    return ans


if __name__ == "__main__":
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
