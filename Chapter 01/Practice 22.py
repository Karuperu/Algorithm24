import queue
a = input('문자열 입력 : ')
b = queue.LifoQueue()
for i in a:
    b.put(i)
print('역순 문자열 : ',end='')
for i in a:
    print(b.get(),end='')