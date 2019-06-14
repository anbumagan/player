m,n=input().split()
m1=int(m)
n1=int(n)
p=(m1//2)-1
c=0
for i in range(1,p+1):
    if(i*p==n1):
        c=c+1
    else:
        p=p-1
if(c>=1):
    print("yes")
else:
    print("no")
