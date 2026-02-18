name = input('Type your name: ')
print('Welcome', name, 'to the adventure!')

answer = input("You are on a dirt road, it has come toan end and you can go left or right. Which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around it or swin to swim accross: ")

    if answer == 'swim':
        print('You swam acrross and were eaten by an alligator.')
    elif answer == 'walk':
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == 'right':
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (Cross/back) ").lower() 
    
    if answer == 'Back':
        print('You got back and lose.')
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (Yes/No) ").lower

        if answer == 'yes':
            print('You talk to the stanger and they give gold. You WIN!')
        elif answer == "no":
            print("You ignored the stranger and they are upset and kill you")
        else:
            print("Not a vaild option. You lose.")
    else:
        print('Not a valid option. You lose.')
print("Thank you for playing", name)