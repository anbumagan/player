
l,m=map(str,input().split())
m=int(m)
c=0
for i in range(0,m):
    if(str(i) in l):
        c=c+1 
if(c==m):
    print("yes")
else:
    print("no")
