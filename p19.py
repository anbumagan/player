import math
n=int(input())
if(n%2==0):
    print("2",end=" ")
    n=n//2
for i in range(3,int(math.sqrt(n))+1):
    while(n%i==0):
        print(i,end=" ")
        n=n//i
    i+i+1    
if n>2:
    print(n,end=" ")
