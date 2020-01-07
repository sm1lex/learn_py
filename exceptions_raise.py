# build own Exception class 

class ShortInputException(Exception):
    ''' A user-defined exception class '''
    def __init__(self, length, atleast):
#        Exception.__init__(self)
        self.length = length
        self. atleast = atleast

try:
    text = input('Input some txt --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('You press <Ctrl+d> programm is closed')
except ShortInputException as ex:
    print('ShortInputException: The input was ' + '{0} long, minimum lengt of input text\
    at least {1}'. format(ex.length, ex.atleast))

else:
    print('No exception was raised!')
    print('You enter: {}'. format(text))

