# Banglore,Hyderabad,Delhi
p = input("Where do live?:")
t = int(input("How many days do you spend?:"))

if ((p=="Banglore" or p=="Hyderabad") and t<=2):
    print("You can go to Udupi")
elif((p=="Banglore" or p=="Hyderabad") and t<=4):
    print("You can go to SriRangam")
elif((p=="Delhi")and t>4):
    print("You can go to SriRangam")

elif((p=="Banglore" or p=="Hyderabad") and t>=4):
    print("You can go to Badariksharama")
elif((p=="Delhi")and t<4):
    print("You can go to  Udupi")

elif((p=="Delhi")and t<2):
    print("You can go to Badariksharama")
else:
    print("Your city is not avalable yet")