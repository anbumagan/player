import numpy
st=str(input())
s=list(st)
l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
g2=numpy.roll(l,3)
g1=list(g2)
for i in st:
    if(i in g1):
        y=g1.index(i)
        print(l[y],end="")
