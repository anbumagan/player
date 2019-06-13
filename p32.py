x,y=map(int,input().split())
z=list(map(int,input().split()))
y1=sorted(z)
if(y in y1):
    print("Yes")
else:
    print("No")
