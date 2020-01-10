import sys
import time

f = None
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        if EOFError:
            print('Could not find file poem.txt')

            
        print(line, end='')
        sys.stdout.flush()
        print('Pls press <Ctrl+c>')
        time.sleep(4)
except EOFError:
    print('You press <Ctrl+d> operations will break')
except IOError:
    print('Could not find file poem.txt')
except KeyboardInterrupt:
    print('You press <Ctrl+c> and cancelled from reading file')
finally:
    if f:
        f.close()
        print('Cleaning system resource, file is closed')
    
