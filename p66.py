x,y=map(int,input().split())
l=list(map(int,input().split()))
c=[]
for j in l:
    d=l.count(j)
    if(d==y):
       c.append(j)
print(*((sorted(set(c))))
