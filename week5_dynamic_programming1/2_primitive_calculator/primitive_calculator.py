# Uses python3
import sys


def optimal_sequence(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i])

        if i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i])

    solution = []
    while n > 1:
        solution.append(n)
        if n % 2 == 0 and dp[n // 2] == dp[n] - 1:
            n = n // 2
        elif n % 3 == 0 and dp[n // 3] == dp[n] - 1:
            n = n // 3
        else:
            n -= 1
    solution.append(1)
    return reversed(solution)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=" ")
