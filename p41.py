n,m=map(int,input().split())
c=0
for i in range(0,n+1):
    if(m**i==n):
        c=c+1
if(c>=1):
    print("yes")
else:
    print("no")
