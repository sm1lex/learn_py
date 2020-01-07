# basic principles of using files

ipsum = '''\
!!!!!!Programming is fun, when the programm is done
if you wanna have a good and interesting job:
    use Python everywere!
'''


# open or creat file and assign this object <f> variable

f = open('poem.txt', 'w')
f.write(ipsum)
f.close()


f = open('poem.txt', 'r')
while True:
    string = f.readline()
    if len(string) == 0:
        break

    print(string, end = '')
f.close()
