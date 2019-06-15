import math
x,y=map(int,input().split())
z=math.factorial(y)*math.factorial(x-y)
print(math.factorial(x)//z)
