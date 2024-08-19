m = int(input()) // 50
n = int(input())
# dp = [[0] * (m + 1) for _ in range(n + 1)]
dp = [[(0, '')] * (m + 1) for _ in range(n + 1)]
data = [0]
for _ in range(n):
    elem = input().split(';')
    data.append([int(elem[0]), int(elem[1]) // 50, elem[-1]])
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # dp[i][j] = max(
        #     dp[i - 1][j],
        #     dp[i - 1][j - data[i][1]] + data[i][0] if j >= data[i][1] else 0
        # )
        dp[i][j] = max(
            dp[i - 1][j],
            (
                dp[i - 1][j - data[i][1]][0] + data[i][0],
                dp[i - 1][j - data[i][1]][-1] + '+' + data[i][-1]
            ) if j >= data[i][1] else (0, ''),
            key=lambda x: x[0]
        )
print(';'.join(dp[-1][-1][-1].split('+')[1:]))