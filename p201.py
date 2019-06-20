def cat(n):
    if(n<=1):
        return 1
    num=0
    for i in range(n):
        num=num+cat(i)*cat(n-i-1)
    return num

a=int(input())
for i in range(a):
    print(cat(i),end=" ")
