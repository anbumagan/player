a,b,c=map(int,input().split())
l=list(map(int,input().split()))
c1=[]
for i in range(b-1,c):
    c1.append(l[i])
print(min(c1)) 
