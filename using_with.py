#use with...as

with open('poem.txt', 'r') as f:
    for read in f:
        print(read, end='')
