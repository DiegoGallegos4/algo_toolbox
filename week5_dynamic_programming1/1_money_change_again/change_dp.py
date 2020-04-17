# Uses python3
import sys


def get_change(m):
    dp = [float("inf")] * (m + 1)
    dp[0] = 0
    coins = [1, 3, 4]
    for i in range(1, m + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i - coin] + 1, dp[i])
    return dp[m]


if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))
