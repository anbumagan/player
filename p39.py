n=int(input())
c=d=0
for i in range(0,10000):
    if(2**i==n):
        c=c+1
    else:
        d=d+1
if(c>=1):
    print("yes")
else:
    print("no")
