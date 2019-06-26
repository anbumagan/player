a=int(input())
b=bin(a)[2:]
b=b[::-1]
for i in range(len(b)):
    if(b[i]=='1'):
        print(i+1)
        break
