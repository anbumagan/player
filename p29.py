import math
x,z=map(int,input().split())
c=0
for i in range(x,z+1):
    if(math.sqrt(i)-math.floor(math.sqrt(i))==0):
        c=c+1
print(c)
