# example input/output and checking word for the palindrom



def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)
   

input_str = input('Enter some word for check: ')

str_intuple = [input_str]
del_symbol =  ['.', '?', '!', ':', ';', '-', '()', '{}', '[]', '!', ' ', '_', ',']
print(str_intuple & del_symbol)

if is_palindrome(input_str):
    print('This is palindrome')
else:
    print('Don\'t worry about this word, this is not palindrome')
