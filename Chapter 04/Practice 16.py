def powerMat(x, n):
    if n == 1:
        return x
    elif (n % 2) == 0:
        return powerMat(multMat(x, x), n // 2)
    else:
        return multMat(x, powerMat(multMat(x, x), (n - 1) // 2))
def multMat(M1, M2):
    temp = [[0] * (len(M1)) for _ in range(len(M2[0]))]
    for i in range(len(M1)):
        for j in range(len(M1[0])):
            for k in range(len(M2[0])):
                temp[i][k] += M1[i][j] * M2[j][k]
    return temp

size = int(input("행렬의 크기를 입력하세요: "))
print("행렬을 입력하세요:")
M = [[int(input()) for _ in range(size)] for _ in range(size)]
n = int(input("거듭제곱할 횟수를 입력하세요: "))
result_power = powerMat(M, n)
print("행렬의 거듭제곱 결과는:")
print(result_power)