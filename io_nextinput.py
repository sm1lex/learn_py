input_str = input('Enter some word for check: ')



#str_intuple = ('some work ! wit a')
del_symbol =  (' ', '!',':', ';', '-', '(', '{}', '[]', '!', '' '', '_', ',', ' ')
del_scope = (["!", " "])
#print(str_intuple & del_symbol)
#print(str_intuple in del_symbol)

modify_str = [input_str] 

for i in input_str:
    if i in del_symbol:
        del i 
    else:
        print(i, end='')
print()
print(input_str)

