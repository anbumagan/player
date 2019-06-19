n=int(input())
l=list(map(int,input().split()))
s=[]
c=[]
for i in range(0,n):
    s=l[:i]
    c.append(sum(s))
c.append(sum(l))
print(*c[1:])
