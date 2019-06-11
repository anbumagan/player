m,n=map(int,input().split())
l=100000
for i in range(1,l):
    if(i%m==0 and i%n==0):
        print(i)
        break
