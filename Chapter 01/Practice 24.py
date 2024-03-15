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