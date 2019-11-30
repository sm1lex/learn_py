#some example how to use references, and don't make a mistake

shoplist = ['apple', 'jam', 'orange', 'potato']
print('Create some shoplist with fructs, and asign this to variables "shoplist"')
print('Them asign this object to new variable new_shoplist')

new_shoplist = shoplist
print('Now we have shoplist {}\nand new_shoplist {}'. format(shoplist, new_shoplist))

print('Then we del 1 item in shoplist, and see what happen with new_shoplist')
del shoplist[0]
print('Now we have shoplist {}\nand new_shoplist {}'. format(shoplist, new_shoplist))

print('Try del 1 item in new_shoplist')
del new_shoplist[0]
print('Now we have shoplist {}\nand new_shoplist {}'. format(shoplist, new_shoplist))

print('Add new object "baba" and asign variables "mybaba" this all slice object')
baba = ['leg', 'head', 'knees', 'body']
mybaba = baba[:]
print('And we have baba {} and mybaba {}'. format(baba, mybaba))

del mybaba[0]
print('And we have baba {} and mybaba {}'. format(baba, mybaba))
print('We see when we asign variables to object we reference to example of object,\nwhen we asign variable all slice object not reference we change them independent')
