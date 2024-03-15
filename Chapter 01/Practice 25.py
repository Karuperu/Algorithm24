list1 = {1, 2, 3, 4, 5}
list2 = {4, 5, 6, 7, 8}
list3 = list1.union(list2)
print('합집합', list3)
list3 = list1.intersection(list2)
print('교집합', list3)
list3 = list1 - list2
print('차집합', list3)