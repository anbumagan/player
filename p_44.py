m,n=input().split()
m1=str(m)
n1=int(n)
k=m[-n1:]+m[:-n1]
print("".join(k),end="")
