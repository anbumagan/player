n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=l[:n]
l2=l[m+1:]
c=[]
if(len(l1)<len(l2)):
    for i in l1:
        if(i in l2):
            c.append(i)
else:
    for i in l2:
        if(i in l1):
            c.append(i)
print(*sorted(set(c)))
