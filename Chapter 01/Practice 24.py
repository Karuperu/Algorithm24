#연습문제 24번
#우선순위 큐를 이용해 리스트속 숫자를 정렬하여 출럭하는 프로그램
#202110807 안치성
import heapq
num=[54, 26, 85, 91, 12, 4, 36, 75, 64, 49]
n = len(num)
h=[]
for i in range(n):
    heapq.heappush(h,num[i])
heapnum = []
for i in range(n):
    heapnum.append(heapq.heappop(h))
print(num)
print(heapnum)