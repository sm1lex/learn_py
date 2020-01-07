# basic example using pickle module for I/O obj in file

import pickle

obj = ['apple', 'banana', 'orange']

f = open('pickle.txt', 'wb')
pickle.dump(obj, f)
f.close()

f = open('pickle.txt', 'rb')
f_out = pickle.load(f)
print(f_out)
f.close()

