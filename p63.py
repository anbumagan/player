x=int(input())
y=list(map(int,input().split()))
z=list(map(int,input().split()))
c=[]
for i in range(0,x):
    if(y[i] in z):
        c.append(y[i])
c1=sorted(set(c))
print(*c1)
