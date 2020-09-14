# Uses python3
import itertools
import sys


def partition3(A):
    num_subsets = 3
    subset_sum = sum(A) // num_subsets
    if sum(A) % num_subsets != 0 or len(A) < num_subsets:
        return 0
    # dp[i][j] could I get i as sum from 0...j items
    dp = [[False] * (len(A) + 1) for _ in range(subset_sum + 1)]
    for j in range(len(A) + 1):
        dp[0][j] = True

    for i in range(1, subset_sum + 1):
        for j in range(1, len(A) + 1):
            # compensate from starting from 1
            item_index = j - 1
            if i - A[item_index] >= 0:
                # i, item_index - 1 -> do not take
                # i - A[item_index] -> take
                dp[i][item_index] = (
                    dp[i][item_index - 1] or dp[i - A[item_index]][item_index - 1]
                )
            else:
                # dont take
                dp[i][item_index] = dp[i][item_index - 1]
    return dp[-1][-1]


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
