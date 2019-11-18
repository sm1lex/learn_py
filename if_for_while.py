#control flow statements of python if/for/while
time = 0
guess = int(input('Enter time of the day, and i show you this time by PM or AM : '))
if (12 > guess >= timei) & (guess == 24):
    # New block starts here
    print('Your time at {} AM  is now'.format(guess))
    # New block ends here
if  (guess == 24):
    print('Your time at {} AM  is now'.format(guess)) 
elif 24 > guess >= 12 :
    # New block starts
    print('Your time at {} PM is now'.format(guess))
else:
    print('Your time is incorrect tipe, please enter number in range[0-24]')
print('Done')
#This last statement is always executed,
#after the if statement is executed
