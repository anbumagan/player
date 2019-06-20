a=int(input())
l=list(map(int,input().split()))
pd=1
for i in l:
    pd*=i
if(pd%2==0):
    print("even")
else:
    print("odd")
