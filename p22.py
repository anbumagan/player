x,y=map(int,input().split())
i=1
s=[]
n=10000
for i in range(1,n+1):
    if(x%i==0 and y%i==0):
        s.append(i)
       
print(max(s))
