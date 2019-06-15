import math
x,y=map(int,input().split())
print(math.factorial(x)//math.factorial(x-y))
