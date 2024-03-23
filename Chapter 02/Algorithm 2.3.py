#자연수의 제곱계산(O(n))
def compute_square_B(n):
    sum = 0
    for i in range(n):
        sum = sum + n
    return sum
print(compute_square_B(int(input("제곱을 구할 수 입력 : "))))