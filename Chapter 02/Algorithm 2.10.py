#이진수 변환에서 총 비트 수 계산(순환 알고리즘)
def binary_digits(n):
    if n <= 1:
        return 1
    else:
        return 1 + binary_digits(n//2)
print(binary_digits(int(input("정수 입력 : "))))