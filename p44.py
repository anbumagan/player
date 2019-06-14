import numpy as np
m,n=input().split()
m1=list(str(m))
n1=int(n)
k=np.roll(m1,3)
print("".join(k))
