# Uses python3
def edit_distance(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    # fill 1st row
    for j in range(len(t) + 1):
        dp[0][j] = j
    # fill 1st col
    for i in range(len(s) + 1):
        dp[i][0] = i

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            ins = dp[i][j - 1] + 1
            delt = dp[i - 1][j] + 1
            # i - 1 & j - 1 to compensate for len(s/t) + 1
            if s[i - 1] == t[j - 1]:
                match = dp[i - 1][j - 1]
            else:
                match = dp[i - 1][j - 1] + 1
            dp[i][j] = min(ins, delt, match)
    # for i in range(len(s) + 1):
    #     print(dp[i])
    return dp[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
