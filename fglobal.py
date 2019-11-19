#example global function
x = 20
print('In the main block x =', x)
def fglobal():
    global x
    print('x in fglobal() =', x)
    x = 11
    print('x in fglobal after change =', x)
fglobal()
print('x in main at the end of programm', x)
