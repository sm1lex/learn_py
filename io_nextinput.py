input_str = input('Enter some word for check: ')



str_intuple = ('some work ! wit a')
del_symbol =  ['?', '!',':', ';', '-', '(', '{}', '[]', '!', '' '', '_', ',']
#print(str_intuple & del_symbol)
#print(str_intuple in del_symbol)

for i in str_intuple:
    if i == '!':

        print(i)
        del i

    print(i, end=' ')

