k=int(input())
a=[int(x) for x in input().split()]
c=a[0]
for i in range(k-1):
    if(c%2==0):
        print(c,end=" ")
        c=c+a[i+1]
    else:
        print(a[i],end=" ")
if(c%2==0):
    print(c)
else:
    print(a[k-1])
