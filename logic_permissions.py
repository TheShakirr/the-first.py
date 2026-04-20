age = int(input("Enter your age: "))
parent = input("is parent with you?(y/n):")
if (age >= 13) or  (age >= 10 and parent == "y"):
    print("OK enter")
else:
    print("sorry not this time")