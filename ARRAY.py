d=[5,56,23,3,37]


i=0
while(i<len(d)):
    d[i]=d[i]+10
    i=i+1


i=0
while(i<len(d)):
    print(d[i])
    i=i+1

sum=0
i=0
while(i<len(d)):
    sum = sum+d[i]
    i=i+1

print("The sum is:", sum)