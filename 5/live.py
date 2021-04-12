def longest(A, B):
    dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
    l = 0

    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j] == 1:
                l += 1
                print(A[i], end='')
                break
    print("\n", l)


A = 'DAMIAN'
B = 'XDITN'
longest(A, B)



def has_subset_of_sum_t(arr: list, t):
    n = len(arr)
    solution = [None] * n
    if t > sum(arr) or t == 0:
        return False
    for i in range(n):
        solution[i] = [False] * (t + 1)
    solution[0][0] = True
    for i in range(1, n):
        for k in range(t):
            solution[i][k] = solution[i-1][k]
            if solution[i - 1][k]:
                if arr[i] + k <= t:
                    solution[i][arr[i] + k] = True
            else:
                solution[i][arr[i]] = True
    for i in range(n):
        if solution[i][t]:
            return True, solution
    return False
print(has_subset_of_sum_t([13, 7, 21, 42, 32, 44, 52], 51))
