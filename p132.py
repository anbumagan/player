a=str(input())
l=[]
c=0 
m=0
for i in range(len(a)-1):
    m=int(a[i])+int(a[i+1]) 
    if(m%2!=0):
        c=c+1 
    else:
        l.append(c)
        c=0
    l.append(c)
c1=max(l)
if(c1==0):
    print("0")
else:
    print(c1+1)
