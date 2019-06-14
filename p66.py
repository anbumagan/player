x,y=map(int,input().split())
l=list(map(int,input().split()))
c=[]
for i in l:
    d=l.count(i)
    if(d==y):
       c.append(i)
print(*(set(c)))
