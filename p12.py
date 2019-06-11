import numpy as np
x,y=map(int,input().split())
l=list(map(int,input().split()))
print(np.roll(l,y))

