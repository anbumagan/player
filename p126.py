a,b=map(int,input().split())
l=list(map(int,input().split()))
c=[]
for i in l:
    if(l.count(i)<b):
        c.append(i)
print(*sorted(set(c)))
