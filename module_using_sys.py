#using sys standard library of python
import sys

print('The command line arguments you input: ')
for i in sys.argv:
    print(i)

print('The PYTHONPATH is', sys.path, '\n')
