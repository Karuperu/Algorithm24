#연습문제 23번
#큐를 사용하여 피보나치 수열을 계산하는 프로그램
#202110807 안치성
from collections import deque
q = deque()
q.append(0)
q.append(1)
print('F(0) = 0')
print('F(1) = 1')
for i in range(2,10):
    a = q.popleft()
    b = q.popleft()
    c = a + b
    q.appendleft(b)
    q.append(c)
    print('F(%d) ='%i, c)