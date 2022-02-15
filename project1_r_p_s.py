import random

def gamewin(com, user):
    if com == user:
        return None
    elif com == 'r':
        if user == 's':
            return False
        elif user == 'p':
            return True
    elif com == 'p':
        if user == 'r':
            return False
        elif user == 's':
            return True
    elif com == 's':
        if user == 'p':
            return False
        elif user == 'r':
            return True

print("Computer Turn...\nComputer Has Choosen!")
randno = random.randint(1,3)
if randno == 1:
    comp = 'r'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 's'

user = input("user Turn - Choose Rock(r), Paper(p), Scissor(s) = ")
a = gamewin(comp, user)

print(f"Computer = {comp}")
print(f"User = {user}")

if a == None:
    print("Game Tie")
elif a:
    print("User Won!")
    print("Computer Loss!")
else:
    print("Computer Won!")
    print("User Lose!")
