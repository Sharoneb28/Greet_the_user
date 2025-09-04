import random
name=input("Enter your name: ")
name2=input("Enter your crush name: ")
percentage=random.randint(1,100)
print(name + " and " + name2 + " have " + str(percentage) + "% love compatibility")
if percentage>70:
    print("You love each other like Romeo and Juliet")
elif percentage>40:
    print("You have a good chance")
else:
    print("Not compatible")