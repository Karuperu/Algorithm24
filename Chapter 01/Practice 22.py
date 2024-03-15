#연습문제 22번
#입력받은 문자열을 역순으로 출력하는 프로그램
#202110807 안치성
import queue
a = input('문자열 입력 : ')
b = queue.LifoQueue()
for i in a:
    b.put(i)
print('역순 문자열 : ',end='')
for i in a:
    print(b.get(),end='')