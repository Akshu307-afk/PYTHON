
pionts1 =0
ans1 = input("What is the name of prahalada's mother?:")
if(ans1=="Kayadu"):
    points1 = pionts1 +5
else:
    print("Incorrect, The answer is kayadu")


ans2 = input("which avatara of vishnu saved prahalada:")
if(ans2=="Narashima") or (ans2=="Narahari"):
    points1 = points1+5
else:
    print("Incorrect,answer is Narashima or Narahari")

print ("you scored", points1, "out of 10")    