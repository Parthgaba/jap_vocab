import requests as rq
import random

r = rq.get('https://raw.github.com/Parthgaba/jap_vocab/master/vocab_dict.py')

py_code = r.text.replace('\n',' ')
print(' REMEMBER CLICK 0 FOR ANS AND 1 FOR EXIT ')
exec(py_code)
l = []
choice = ''
inp = ''
while(1):
    l = list(my_vocab.keys())
    choice = random.choice(l)
    print(choice)
    inp = input()
    if inp=='0':
        print(my_vocab.get(choice))
    elif inp=='1':
        break
    
