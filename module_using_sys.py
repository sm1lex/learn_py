#using sys standard library of python
import sys
import os

print('The command line arguments you input: ')
for i in sys.argv:
    print(i)

print('The PYTHONPATH is', sys.path, '\n')

print(os.getcwd())
