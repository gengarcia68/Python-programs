import random
#ask user to pick a number
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)    
#loop if the number is not an int
    if top_of_range <=0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time. ')
    quit()
#check if you guess correct
random_number = random.randint(0, top_of_range)
guesses = 0
#loop to ask user to guess number
while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time. ")
        continue    
  #check if guess is correct
  #   
    if user_guess == random_number:
        print('You got it!')
        print( 'It took you',guesses, 'guesses to get it right')
        break
    
        #loop if the number is higher or lower
    elif  user_guess > random_number:
        print("You were above the number!")
    else:
        print('You were below the number!')
        print('You got it wrong! ')
        

