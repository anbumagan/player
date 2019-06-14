x=int(input())
c=0
for i in range(2,x):
    if(x%i==0):
        c=c+1
if(c>=1):
    print("yes")
else:
    print("no")
