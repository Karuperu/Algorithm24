#이진수 변환에서 총 비트 수 계산(반복 알고리즘)
def binary_digits(n):
    count = 1
    while n>1:
        count = count + 1
        n = n // 2
    return count
print(binary_digits(int(input("정수 입력 : "))))