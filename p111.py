n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=l[:n]
l2=[]
for i in range(n,len(l)):
    l2.append(l[i])
c=[]
if(len(l1)<len(l2)):
    for j in l1:
        if(j in l2):
            c.append(j)
    print(*sorted(c))
else:
    for i in l2:
        if(i in l1):
            c.append(i)
    print(*sorted(c))
