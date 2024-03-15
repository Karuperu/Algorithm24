#연습문제 5번
#알고리즘 1.7을 수정하여 출럭하는 프로그램
#202110807 안치성
def gcd(a, b):
    print('gcd', (a,b))
    while b != 0:
        r = a % b
        a = b
        b = r
        print('gcd', (a,b))
    return a
print('60과 28의 최대공약수 =', gcd(60,28))