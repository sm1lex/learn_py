#function return with value
a = input('Enter some number ')
b = input('Enter next number ')
def evaluate(x, y):
    x = a
    y = b
    if x > y:
        print('x is higher than y')
        return x
    elif x == y:
        print('x equal y')
        return 'The number are equal'
    else:
        print('y is higher then x')
        return y
    
print(evaluate(a, b))

def somefun():
    pass

print(somefun())
