z=int(input())
l=list(map(int,input().split()))
a=len(l)
if(a%2!=0):
    c=(a-1)//2
    l1,l2=l[0:c],l[c:]
    print(*sorted(l1),end=" ")
    l2=sorted(l2)
    print(*l2[::-1])
else: 
    c=(a)//2
    l1,l2=l[0:c],l[c:]
    print(*sorted(l1),end=" ")
    l2=sorted(l2)
    print(*l2[::-1])
