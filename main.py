import random

num=input('type a number : ')
if num.isdigit():
    num=int(num)

    if num<=0:
        print('please print a number bigger than 0 ')
        quit()
else :
    print('typer another number ')
    quit()
random_number=random.randint(0,num)
print(random_number)

guesses = 0

while True :
    guesses += 1
    user_guess=input('make a guess ')
    if user_guess.isdigit():
        user_guess= int(user_guess)

    else:
        print('typer another number ')
        continue

    if user_guess == random_number :
        print('YOU GO IT')
        break
    else :
        print('unfortunately ')
print("you got ",guesses ,'gussses')
