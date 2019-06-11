import numpy as np
x,y=map(int,input().split())
l1=list(map(int,input().split()))
print(np.roll(l1,y))

