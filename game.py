import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=='rock':
        you=='scissor'
        return False
        if you=='paper':
            return True

    elif comp=='paper':
        you=='rock'
        return False
        if you=='scissor':
            return True

    elif comp=='scissor':
        you=='paper'
        return False
        if you=='rock':
            return True



print("Comp turn : ")
ran=random.randint(1,3)
if ran==1:
    comp='rock'
elif ran==2:
    comp='paper'
elif ran==3:
    comp='scissor'


you=input("Enter your choice: ")
a=game(comp,you)


print(f'Computer chose: {comp}')
print(f'You chose: {you}')

if a==None:
    print("Game is tie!")
elif a:
    print("You win") 
else:
    print("You lose!")


