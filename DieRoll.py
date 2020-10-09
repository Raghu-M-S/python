from random import randint
q=input("Do you want to roll the die?? Y/N")

while "Y"==input():
    print(f"The rolled die is.....{randint(1,6)}")
else:
    print("Thank you for playing")
