import random

def game(comp, user):

    # If 2 values are equal, declare a tie.
    if(comp==user):
        print("It's a tie!")
    # Check for all the possibilities when the computer chooses 's'.
    elif(comp=="s"):
        if(user=="w"):
            print("Computer chose Snake!")
            print("You chose Water!")
            print("Computer won!")
        elif(user=="g"):
            print("Computer chose Snake!")
            print("You chose Gun!")
            print("You won!")
    # Check for all the possibilities when the computer chooses 'w'.
    elif(comp=="w"):
        if(user=="s"):
            print("Computer chose Water!")
            print("You chose Snake!")
            print("You won!")
        elif(user=="g"):
            print("Computer chose Water!")
            print("You chose Gun!")
            print("Computer won!")
    # Check for all the possibilities when the computer chooses 'g'.
    elif(comp=="g"):
        if(user=="s"):
            print("Computer chose Gun!")
            print("You chose Snake!")
            print("Computer won!")
        elif(user=="w"):
            print("Computer chose Gun!")
            print("You chose Water!")
            print("You won!")


print("Computer's Turn: s(Snake), w(Water) or g(Gun)?")

randNo = random.randint(1, 3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"

user = input("Your Turn: s(Snake), w(Water) or g(Gun)?\n")

if(user=="s" or user=="w" or user=="g"):
    game(comp, user)
else:
    print("Invalid Entry! Please try again later.")



