#while example in python
#while statement is an example of what is called looping
number = 12
running = True

while running:
    guess = int(input('Enter and try guessed my number : '))

    if guess == number:
        print('Congrats, you guessed this number.')
        running = False
    elif guess < number:
        print('Try enter a higher number.')
    else:
        print('Try enter a lower number.')
else:
    print('The while loop is over.')
print('Ye boy.You looks like a shaman.')
