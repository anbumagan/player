a1,b=map(int,input().split())
l=list(map(int,input().split()))
if(b in l):
    print("yes",end=" ")
    print(l.count(b))
else:
    print("no")
