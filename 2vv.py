from itertools import combinations
vijay,v1=input().split()
v1=int(v1)
m=[]
dd=combinations(vijay,len(vijay)-v1)
for i in list(dd):
  m.append("".join(i))
print(min(m))
