vk=int(input())
vj=[]
for i in range(0,l1):
 inpu=input()
 vj.append(inpu)
vk=[]
for i in zip(*vj):
 if(i.count(i[0])==len(i)):
  vk.append(i[0])
            
 else:
  break
print(''.join(vk))
