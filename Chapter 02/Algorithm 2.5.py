#리스트의 중복 항목 탐색
def unique_elements(A):
    n = len(A)
    for i in range(n-1):
        for j in range(i+1,n):
            if A[i] == A[j]:
                return False
    return True
a = [32, 14 ,5, 17, 23, 9, 11, 14, 26, 29]
b = [13, 6, 8, 7, 12, 25]
print(a, unique_elements(a))
print(b, unique_elements(b))