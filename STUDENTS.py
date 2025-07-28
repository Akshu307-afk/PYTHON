st = []

n = int(input("Enter how many students:"))

i=0
while(i<n):
    s = input("Enter the student name:")
    st.append(s)
    i=i+1

print("The students are:")
i=0
while(i<len(st)):
    print(st[i])
    i=i+1

if("Akshobhya" in st):
    print("Akshobhya is present")
    st.remove("Akshobhya")
else:
    print("Akshobhya is not present")