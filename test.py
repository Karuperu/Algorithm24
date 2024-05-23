M=13
table = [None]* M
def hashFn(key):
    return key % M
def lp_insert(key):
    id = hashFn(key)
    count = M
    while count>0 and (table[id] != None and table[id] != -1):
        id = (id + 1 + M)%M
        count -= 1
    if count > 0:
        table[id] = key
    return

def lp_search(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None:
            return None
        if table[id] != -1 and table[id] == key :
            return table[id]
        id = (id + 1 + M) % M
        count -= 1
    return None

def lp_delete(key) :
    id = hashFn(key) 
    count =M
    while count > 0:
        if table[id] == None : return
        if table[id] != -1 and table[id] == key :
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1
def hashFn(key):
    sum=0
    for c in key:
        sum=sum+ord(c)
    return sum%M
print("최초:", table)

lp_insert("aaaa"); print("aaaa 삽입:", table)
lp_insert("adf"); print("adf 삽입:", table)
lp_insert("dqdf"); print("dqdf 삽입:", table)
lp_insert("htwwthe"); print("htwwthe 삽입:", table)
lp_insert("gzas"); print("gzas 삽입:", table)
lp_insert("tqee"); print("tqee 삽입:", table)
lp_insert("oiut"); print("oiut 삽입:", table)
lp_insert("pahe"); print("pahe 삽입:", table)
lp_insert("zere"); print("zere 삽입:", table)
lp_delete("qiso"); print("qiso 삭제:", table)

print("aaaa 탐색:", lp_search("aaaa"))