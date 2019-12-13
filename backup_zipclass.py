#create mini-backup programm with implement native python3 zipfile class

#before testing some methods
from zipfile import ZipFile 
import os

with ZipFile('/home/aleksey/Documents/test.zip', 'w') as myzip:
   myzip.write('/home/aleksey/Documents/test.txt')


#file = open('/home/aleksey/Documents/test.txt', 'w')
#file.write('Happy New Year')
#file.close


with open('/home/aleksey/Documents/test.txt', 'a') as file:
    file.write('iood morning superman')
cmd = 'cat /home/aleksey/Documents/test.txt'
print(cmd)
print(cmd)
