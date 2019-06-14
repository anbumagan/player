x=int(input())       
y=list(map(int,input().split()))
i=0
count=1
m=count
f=1
for i in range(x-1):
    if(y[i]==y[i+1]):
        count=count+1
        f=count
    elif(count>m):
        m=count
        f=count
        count=1
print(f) 
