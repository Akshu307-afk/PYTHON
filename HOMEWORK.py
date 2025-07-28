
ans =1
while(ans==1 or ans==3):
    ans = int(input("Enter 1 if you have pending work, 2 if you have finshed the homework3if you want to play"))
    if (ans==1):
        print("pls finshe your hw")
    elif(ans==3):
        print("you can only play after finshing hw")
    elif(ans==2):
        print("You can do whatever you want")