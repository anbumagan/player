x=int(input())
l=list(map(int,input().split()))
d1=l[0]
for i in range(1,x):
    d1=d1^l[i]   
print(d1)
