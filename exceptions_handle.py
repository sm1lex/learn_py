# try ... except statement

try:
    text = input("Enter something --> ")
except EOFError:
    print('Are yuo kidding me why you push <Ctrl+d>')
except KeyboardInterrupt:
    print('OMG why you push <Ctrl+c>')
else:
    print('You enter {}'. format(text))

