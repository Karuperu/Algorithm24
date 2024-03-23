#자연수의 제곱계산(O(n^2))
def compute_square_C(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum = sum + 1
    return sum
print(compute_square_C(int(input("제곱을 구할 수 입력 : "))))