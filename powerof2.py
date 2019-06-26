a=int(input())
c=[]
for i in range(0,1000):
    if(2**i==a):
        c.append(i)
if(len(c)==0):
    print("no")
else:
    print("yes")
