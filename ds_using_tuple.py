#some example how we can using tuple in python

#major future of tuple is that they immutable like strings, you can't modify tuple

zoo = ('pyhton', 'elephant', 'giraff')
print('My zoo consists of', len(zoo), 'animals')

new_zoo = ('monkey', 'pingun', zoo)
print('Number of animals in new_zoo is', len(new_zoo))
print('But we summary zoo and new_zoo, and new_zoo consist', new_zoo)

print('First animal in new_zoo is', new_zoo[0])
print('Third animal in new_zoo is', new_zoo[2])
print('If we want show in tuple object we use new_zoo[2][2] abreviation, and this animal is', new_zoo[2][2])

