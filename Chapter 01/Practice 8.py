a = int(input('a = ? '))
b = int(input('b = ? '))
for i in range(max(a,b),(a*b)+1):
    if i % a == 0 and i % b == 0:
        print(i)
        break