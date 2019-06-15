x=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
for i in range(x):
    if(l[i]%2==0):
        c.append(l[i])
    else:
        d.append(l[i])
if(len(c)==1):        
    print(*c)
else:
    print(*d)
