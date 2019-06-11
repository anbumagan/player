n=str(input())
l=list(n)
f={}
for i in l:
    a=l.count(i)
    f[a]=i
g=max(f)
print(f[g])
