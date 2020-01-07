# how use another encoding rule
# encoding=utf-8

import io

f = io.open('poem.txt', 'wt', encoding = 'utf-8')

f.write(u'чмо, сука блеать э')
f.close()

f_out = io.open('poem.txt', 'r', encoding = 'utf-8')

print(f_out.read())
