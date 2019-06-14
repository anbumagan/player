x=int(input())
y=input()
i=0
a1=""
a0=""
for i in range(len(y)):
    if(y[i]=="1"):
        a1=a1+y[i]+" "
    elif(y[i]=="0"):
        a0=a0+a1
        a1=""
print(a0.strip()) 
