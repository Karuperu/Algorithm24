#반복알고리즘 팩토리얼
def factorial(n):
    result = 1
    for k in range(n, 0, -1):
        result = result * k
    return result
num = factorial(int(input("팩토리얼을 구할 수 입력 : ")))
print(num)