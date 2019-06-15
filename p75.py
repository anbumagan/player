x=int(input())
l=list(map(int,input().split()))
c=0
for i in range(x-1):
    for j in range(i+1,x):
        if(l[i]<l[j]):
            c=c+1
print(c)
