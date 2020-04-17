# Uses python3
import sys


def optimal_weight(W, w):
    dp = [[0] * (W + 1) for _ in range(len(w) + 1)]
    for capacity in range(1, W + 1):
        for i in range(1, len(w) + 1):
            # dont take item
            dp[i][capacity] = dp[i - 1][capacity]
            if w[i - 1] <= capacity:
                # choose between taking item and dont take
                dp[i][capacity] = max(
                    dp[i - 1][capacity - w[i - 1]] + w[i - 1], dp[i][capacity]
                )
    print(dp)
    return dp[len(w)][W]


if __name__ == "__main__":
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
