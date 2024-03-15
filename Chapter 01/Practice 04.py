#연습문제 4번
#알고리즘 1.7의 중간값과 결과값을 출럭하는 프로그램
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