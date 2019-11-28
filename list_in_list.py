#list in list test

print('Now we try put one list at another')

first_list = ['apple', 'mango', 'orange']
second_list = [1, 2, 3]
third_list = [ 'opa', 'jopa', second_list]

print('first_list is', first_list, 'and this list have', len(first_list), 'item')
print('second_list is', second_list, 'and this list have', len(second_list), 'item')
print('third_list is and he include second_list', third_list, 'and this list have', len(third_list), 'item')
summ_list = first_list + second_list
print('Now we summary first_list + second_list and we get', summ_list, 'and this summ list have', len(summ_list), 'item')

print('Can we summary int 1, 2, 3 with \'apple\'')

#summ_item = first_list[0] + second_list[1]
#print('This summary equal', summ_item) and we have type error str we can't summary with int classes
summ_item = first_list[0] +third_list[1]
print('This summary equal', summ_item)
