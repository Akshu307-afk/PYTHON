c = input("Have you finished homework (yes/no):")
m = int(input("How many minutes have you played?:"))

if(c=="yes" and m >=30):
    print("We can start coding now!")
elif(c=="no" and m <=30):
    print("Finish your homework, and get some fresh air")
elif(c=="yes" and m <=30):
    print("Get some fresh air")
else:
    print("Finish your homework")
