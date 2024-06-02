def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > w:
                A[i][w] = A[i-1][w]
            else:
                valWith = val[i-1] + A[i-1][w - wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)
    return A[n][W]
def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                A[i][w] = A[i - 1][w]
            else:
                valWith = val[i - 1] + A[i - 1][w - wt[i - 1]]
                valWithout = A[i - 1][w]
                A[i][w] = max(valWith, valWithout)
    for result in A:
        print(result)
    return A[n][W]
W = 6
wt = [3, 2, 1, 4, 5]
val = [26, 20, 14, 40, 50]
n = len(wt)

max_value = knapSack_dp(W, wt, val, n)
print(f"배낭에 담을 수 있는 최대 가치는 {max_value}입니다.")