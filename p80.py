x=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(x):
    for j in range(i+1,x):
        d=abs(l[i]-l[j])
        c.append(d)
if(min(c)==0):
    print("1")
else:print(min(c))
