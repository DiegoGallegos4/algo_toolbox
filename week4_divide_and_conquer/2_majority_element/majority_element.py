# Uses python3
import sys


def get_majority_element(a, lo, n):
    def count_in_subarray(a, lo, hi, x):
        count = 0
        for i in range(lo, hi + 1):
            if a[i] == x:
                count += 1
        return count

    def _get_majority_element(a, lo, hi):
        if lo == hi:
            return a[lo]

        mid = (hi - lo) // 2 + lo
        left = _get_majority_element(a, lo, mid)
        right = _get_majority_element(a, mid + 1, hi)

        if left == right:
            return left

        left_count = count_in_subarray(a, lo, hi, left)
        right_count = count_in_subarray(a, lo, hi, right)
        return max(left_count, right_count)

    majority_count = _get_majority_element(a, 0, n - 1)
    if majority_count >= (n + 1) // 2:
        return majority_count
    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
