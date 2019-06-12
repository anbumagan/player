x,y=map(int,input().split())
z=list(map(int,input().split()))
a=list(map(int,input().split()))
for j in a:
    z.append(j)
    print(max(z),end=" ")
