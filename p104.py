n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n-1):
    s=s+l[i]+l[i+1]
print(s)
