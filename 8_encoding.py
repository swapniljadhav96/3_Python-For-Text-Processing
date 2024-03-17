# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:33:17 2024

@author: suraj
"""



'''-------------22/8/23--8.00--------------------------------(encoding)'''
#UTF:-unicode transformation formatating
#utf-8=8 means 8bits
#encoding
 
string1='apple'
string2='jeei123'
string3='12345'
string4='pre@12'
string1.encode(encoding='UTF-8',errors='strict')
string2.encode(encoding='UTF-8',errors='strict')
string3.encode(encoding='UTF-8',errors='strict')
string4.encode(encoding='UTF-8',errors='strict')


string= 'one 🐘 and three 🐋'
print(string)
print(len(string))


e=string.encode('utf8')
print(e)
print(len(e))

e=string.encode('utf16')
print(e)
print(len(e))

#decodeing
#decodeing for utf8
fname='data.txt'
with open(fname,mode='rb') as f:
    contents=f.read()
    print(contents)
    print(type(contents))
    
    print(contents.decode('utf8'))

#decode for uft16
fname='data.txt'
with open(fname,mode='rb') as f:
    contents=f.read()
    print(contents)
    print(type(contents))
    
    print(contents.decode('utf16'))

##################################

#whitespace stripping
s='     hello world     \n'
s.strip()
s.lstrip()
s.rstrip()


#charater striping
t='--------------hello======='
t.lstrip('-')
t.rstrip('=')
t.strip('-=')

s='     hello world     \n'
s=s.strip()
s
s.replace(' ','')

import re
re.sub('\s+',' ',s)


##############################
#aligning the text string
text='hello world'
text.ljust(29)      #left align
text.rjust(20)      #right align
text.center(20)     #centre align

#all this are feature engineering tecqnique
text.ljust(20,'=')

text.center(20,'*')

# above can be used by using the format methode
format(text,'>20')
#left format
format(text,'<20')
#right format
format(text,'^20')
#center format

# formmat for the charater
format(text,'=>20s')

format(text,'*^20s')

# theses format code can also be used in the format method()
'{:>10s} {:>10s}'.format('hello','world')

#format method()
x=1.23456
format(x,'>10')
x

format(x,'^10.2f')

# Join
parts=['Is','chicago','Not','chicago?']
' '.join(parts)


'Is Chicago Not Chicago?'
','.join(parts)
'Is,Chicago,Not,Chicago?'
'IsChicagoNotChicago?'

# If you joim very few strings then can use + operator
a='Is Chicago'
b='Not Chicago'
a+ " "+ b

