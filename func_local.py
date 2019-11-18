#use local variables and see how work scope of the variables
x = 40
def localf(x):
    print('x is ', x)
    x = 2           #declare local variable of x
    print('New local x is', x)

localf(x)
print('x is still', x)
