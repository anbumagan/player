n=int(input())
m=list(map(int,input().split()))
c=0
if(m==sorted(m)):
    print("yes")
else:
    print("no")
