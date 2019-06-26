a,a1=map(int,input().split())
b=[]
c=[]
for i in range(0,a):
    b.append(input())
for j in range(len(b)-1):
    if(b[j]==b[j+1]):
        c.append(b[j])
        c.append(b[j+1])
if(len(c)==0):
    print("no")
else:
    print("yes")
