#연습문제 8번
#최소공배수를 계산하여 출럭하는 프로그램
#202110807 안치성
a = int(input('a = ? '))
b = int(input('b = ? '))
for i in range(max(a,b),(a*b)+1):
    if i % a == 0 and i % b == 0:
        print(i)
        break