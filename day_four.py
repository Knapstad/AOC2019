len(pass)==6
range(240298, 784956)

def is_valid(numb):
    prev = 0
    counts={}
    if len(str(numb))!=6:
        return False
    for i in str(numb):
        counts[i]=counts.get(i,0)+1
        if i < str(prev):
            return False
        prev = i
    return 2 in counts.values()

count=0
for i in range(240298, 784956):
    if is_valid(i):
        count+=1