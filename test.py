def count_substr(str, a, b):
    count = 0
    n = len(str)
    for i in range (n - 1):
        if str[i] == a:
            for j in range (i + 1, n):
                if str[j] == b:
                    count += 1
    return count

input = "ADBAAEDBA"
result = count_substr(input, 'A', 'B')
print("서로 다른 부분 문자열의 개수: ",result)