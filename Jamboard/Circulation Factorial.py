def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = factorial(int(input("팩토리얼을 구할 수 입력 : ")))
print(num)