n,m=map(int,input().split())
c=[]
for i in range(n,m+1):
    if(i%2!=0):
        c.append(i)
print(sum(c)) 
