import numpy as np
x,y=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(np.roll(l1,y))
print(*l2)
