n=int(input())
l=list(map(int,input().split()))
s=[]
c=[]
d=[]
e=[]
for i in range(0,n):
    s=l[:i]
    c.append(sum(s))
c.append(sum(l))
c=c[1:]
d=c[::-1]
for i in range(len(c)):
    e.append(c[i]+d[i])
print(*e)
