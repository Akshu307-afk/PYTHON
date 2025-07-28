n = int(input("Till which number should i count?:"))

i=1
sum=0
while(i<=n):
    user_num = int(input("Enter the numbers:"))
    sum = sum + user_num
    i = i+1

print("The sum is:", sum)