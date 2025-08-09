import sys
name = str(input("Pls enter your name \t"))
Gender = str(input("Pls enter your Gender \t"))
if Gender == "male" or Gender== "Male":
    print(f"Your name is {name} and Your gender is {Gender}")
elif Gender == "female" or Gender== "Female":
    print(f"Your name is {name} and Your gender is {Gender}")
    print(f"Your name is {name} and Your gender is {Gender}")
else:
    print(f"Pls enter valid gender {Gender} is not valid")
    sys.exit()

print( f"Welcome {name} for driveing licence test lets begain the test")

Proceding = str(input("yes/no \t" ))
if Proceding == "yes" or Proceding == "Yes":
    print(f"Congrulation {name} You can begain the age test")
else:
    print(f"sorry {name} You cant move forward")
    sys.exit()
age = int(input("pls enter your age \t"))
if age > 18:
    print(f"Congrulation {name} You clear the age test")
elif age == 18:
    print(f"We will have to check you {name}")
elif age < 18:
    print(f"sorry {name} you  cant drive")
    sys.exit()

else:
    sys.exit()


print(f"{name} Lets move on to the final test")
print(f"{name} First question")
print(f"{name} Have u ever drive before")

Answers = str(input("Pls just one word answer Yes/No \t"))



if Answers == "Yes" or Answers == "yes":
    print(f"{name} Ok but still u will have to give the driving test")
else:
    print("Dont worry u can join our driving school")
print(f"{name} Do u Have learning drive licence")
Answers = str(input("Pls just one word answer Yes/No \t"))
if Answers == "Yes" or Answers == "yes":
    print(f"{name} Ok thats great")
else:
    print("Sorry u need to make that first")
    sys.exit()

print(f"{name} congratulations you have sucessfully cleared this test u can come to your nearest rto for driving test")
sys.exit()



