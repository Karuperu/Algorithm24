#연습문제 3번
#알고리즘 1.6을 사용하여 최대공약수를 출럭하는 프로그램
#202110807 안치성
def gcd(a, b):
    alist = []
    for i in range(1, a+1) :
        if a % i == 0 :
            alist.append(i)
    print(a, '의 약수 =', alist)
    for i in range(len(alist)-1, 0, -1):
        if b % alist[i] == 0:
            return alist[i]
print('60과 28의 최대 공약수 = ',gcd(60, 28))