ce = input("Is your event for charity(Yes/No):")
fe = int(input("How much are you going to pay?:"))

if(ce == "Yes" or ce== "yes" or fe >=8000):
    print("Thanks, Keshav will come to your concert")
else:
    print("You have to pay 8000 or more")