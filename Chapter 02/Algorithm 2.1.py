#순차 탐색
def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1
A = [32, 14, 5, 17, 23, 9, 11, 4, 26, 29]
key = int(input("Key 입력 : "))
print(sequential_search(A, key))