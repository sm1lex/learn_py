#example how to use <startswith>, <find>, <join>, <if .. in> methods in str class

#create str object
name = 'Smilove_Aleksey'

if name.startswith('Smil'):
    print('Ye this is true, and your name start "Smil"')

if 'ilo' in name:
    print('Yes it contains "ilo" also')

if  name.find('Ale') != -1:
    print('Yes name contains "Ale" also')

delimeter = '_*_'
words = ['alpachino', 'hubabuba', 'opajopa']
print(delimeter.join(words))
