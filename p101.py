a=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(a-1):
    if(l[i]<l[i+1]):
        sum=sum+l[i+1]
print(sum) 
