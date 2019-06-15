x=int(input())
d=1
c=[]
l=list(map(int,input().split()))
for i in range(0,x-1):
    if(l[i]<l[i+1]):
        d=d+1
    else:
        c.append(d)
        d=1
c.append(d)
print(max(c))
