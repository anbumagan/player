x=input()
l=list(map(str,input().split()))
y=sorted(l,key=len)
for i in range(len(y)-1):
    if(len(y[i])==len(y[i+1]) and y[i]>y[i+1]):
        y[i],y[i+1]=y[i+1],y[i]
print(*y)
