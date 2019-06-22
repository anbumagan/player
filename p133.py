a,b=map(int,input().split())
l=[]
c1=[]
for i in range(0,a):
    c,d=map(int,input().split())
    l.append(c)
    l.append(d)
for i in range(len(l)-1):
    for j in range(l[i],l[i+1]+1):
        c1.append(j)
if(b in c1):
    print("yes")
else:
    print("no")
