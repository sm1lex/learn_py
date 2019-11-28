#some example how to using dictionary

#initialize some values and equal them dictionary sequences

ab = {
'Mr.Johny': '+375295334433',
'Sofiya': '+375336688770',
'Smilove': '+375445141228'
}

print('Mr.Johny mobile phone is', ab['Mr.Johny'])

#Deleting some items in dictionary ( key-value)

del ab['Smilove']

print('Now in address book {} contacts'. format(len(ab)))

for name, phone in ab.items():
    print('Contact {} have phone {}'. format(name, phone))

ab['Mortal Combat'] = '+37566666666'

print('Now we added one contact, and now in address book {}'. format(len(ab)), 'contacts')

for name, phone in ab.items():
    print('Contact {} his number {}'. format(name, phone))
 
if 'Sofiya' in ab:
    print('Sofiya number is', ab['Sofiya'])
else:
    print('You writen incorrect name')
