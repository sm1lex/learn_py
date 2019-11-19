#break statement in while loop
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('To small length')
        continue 
    print ('Length of the string is', len(s))
else:
    print ('Common every body i hack the system')
print('Done')
