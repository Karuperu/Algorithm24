#연습문제 20번
#두개의 리스트에 같은항목을 찾는 프로그램
#202110807 안치성
def match(a, b):
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i] == b[j]:
                return True
            else:
                continue
    return False

alist = list(map(int, input('A리스트 ').split()))
blist = list(map(int, input('B리스트 ').split()))
print(alist)
print(blist)
print(match(alist, blist))