x = int(input("Enter the number:"))

y=2
isprime=True
while(y<x):
    if(x %y ==0):
        isprime=False
        print("The number is diviseible by", y)
        print("The number is composite")
    y = y+1

if(isprime==True):
    print("The number is prime") 