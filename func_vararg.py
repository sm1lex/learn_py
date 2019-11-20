#Function with variable number of arguments
def total(a=5, *numbers, **phonebook):
    print('a', a)
    for num in numbers:
        print('num', num)
    for name, phone in phonebook.items():
        print('Name', name,'phone', phone)
total(10, 1,2,3, Jack=2123, Mam=34334, Dad=23432)
