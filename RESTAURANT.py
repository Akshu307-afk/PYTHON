total = 0
x = 0
print("-------------------Welcome to Anagha's Grand restaurant---------------------------")

while(x!=5):
    x = int(input("For dose Enter 1, for Idli enter 2, for extra chutney enter 3, for ice-cream enter 4, for bill enter 5:"))
    if(x==1):
        print("Here is your dose.Cost is 50 Rupees")
        total = total + 50
    elif(x==2):
        print ("Here is your Idli. Cost is 25 Rupees")
        total = total + 25
    elif(x==3):
        print("Here is your Extra Chutney. Cost is 5rupees")
        total = total + 5
    elif(x==4):
        print("Here is your Ice-cream. Cost is 100rupees")
        total = total+100
    elif(x==5):
        print(total,"Ram Ram")