x,y=map(int,input().split())
z=list(map(int,input().split()))
a=list(map(int,input().split()))
for i in a:
    z.append(i)
    print(max(z),end=" ")
