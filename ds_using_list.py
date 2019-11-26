# Using list 
# Create my shop list

myshoplist = ['apple', 'jam', 'mango', 'coconuts']

# Show item in my shop list, and how much item at them

print('In my shop list i have', len(myshoplist), 'item and products.')

print('This products is', end=' ')
for item in myshoplist:
    print(item, end = ' ')

# Append one item in list

print('\nOo I\'m so sorry, i just forgot a milk, and icecream')

myshoplist.append('milk')
myshoplist.append('icecream')
print('Here we are, all is fine, and my list now :', myshoplist)

# Sort list and show

print('Now i\'m sort list')
myshoplist.sort()
print('Its look better in alphabet', myshoplist)
# When you buy item, you delete him at yours list, show this
print('Ok I bought', myshoplist[0])
olditem = myshoplist[0]
del myshoplist[0]
print('And now i can correct, and cross out the item in the list', olditem)
print('My shopping list now have', len(myshoplist), 'item')
print('List now have only', end=' ')
for item in myshoplist:
    print(item, end=' ')

print('\n')
