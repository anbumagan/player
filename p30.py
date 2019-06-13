a,b,c=input().split()
x1=str(a)
y1=str(b)
z=int(c)
c=0
for i in range(len(x1)):
    if(x1[i]!=y1[i]):
        c=c+1 
if(z==c):
    print("yes")
else:
    print("no")
