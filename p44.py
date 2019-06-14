m,n=input().split()
m1=list(str(m))
n1=int(n)
k=m1[n1:]+m1[:n1]
print("".join(k),end="")
