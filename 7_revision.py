# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:32:31 2024

@author: suraj
"""


#day 21/8/23
#revision :- tokenization
#defgragmentation
import re
filename='spam.txt'
filename.endswith('.txt')

area_name='6 lane west andheri'
area_name.endswith('west andheri')

choises=('http:','ftp:')
url='http://www.python.org'
url.startswith(choises)

#taking the or spliting the  string and checking from
#tthe starting or ending index value
#inetrview Question
s='abcdefghi'
print(s[2:7])       #positive indexing

print(s[-7:-2])     # negative indexing

print(s[2:-5])     #negative and positive indexing

#step of the value
print(s[2:7:2])     #positive step value 

print(s[2:7:-2])    #negative step value

print(s[:5])#starting value are not given then it start with the 0 index

print(s[2:])

#reversing the string
print(s[: :-1])

filename='spam.txt'
filename[-4:]=='.txt'

url='http.//www.python.org'
url[:6]=='http' or url[:7]=='https' or url[:4]=='ftps'

#imp ready refererence
from fnmatch import fnmatch,fnmatchcase
names=['Dat1.csv','Dat2.csv','config.ini','top.csv','foo.py','dat1.csv']
[name for name in names if fnmatch(name,'Dat*.csv')]

from fnmatch import fnmatch,fnmatchcase
names=['andher east','parle east','dadar west']
[name for name in names if fnmatch(name,'* east')]



'''-----------------3.00--21/8/23--------------------------------'''
text='yeah,but no, but yeah,but no,but yeah'
#exact match
text=='yeah'
#false
#match at start or end
text.startswith('yeah')

text.endswith('no')
#false

#searching the occurance of the first index of that word in the strig

text.find('no')


#############
#checking for the time matching withe re package

text1='27/11/2012'
text2='Nov 27,2012'

import re
if re.match(r'\d+/\d+/\d+',text1):      #\d+ means match one or more charetre
    print('yes')
else:
    print('no')
        
import re
if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')

#########################
import re
datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat,text1):
    print('yes')      
else:
    print('no')

datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat,text2):
    print('yes')      
else:
    print('no')

#########################
#searching and replacing the text
text='yeah,but no, but yeah,but no,but yeah'
text.replace('yeah','yep')

####################################
#changing the patter of the date in the string  by using the 
#sub function

text='Today is 11/27/2012. Py can starts 3/13/2012'
import re
re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)   #\3 is the 3rd group \1 ist the first group \2 id=s the 2nd group

#if you want to know how many substuititution are done in the text
newtext,n =datepat.subn(r'\3-\1-\2',text)
newtext
n           #how many substitution we did


################################
#checkking the letter in the text 
text='UPPER PYTHON,lower python,mixed Python'
re.findall('python',text,flags=re.IGNORECASE) 

# to substitute
re.sub('python','snake',text,flags=re.IGNORECASE)
#Out[26]: 'UPPER snake,lower snake,mixed snake'
#here are the camel case convention are used

###########################
# now we want to take the letter as  the given in the text such as upper letter or in the lower letter 
#or in the mixed capital letter then we used the function defination 
import re
#import string
#mport nltk
text='UPPER PYTHON, lower python ,Mixed Python'
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else :
            return word
    return replace
text3=re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
text3

#############################
# extraxct from text
str_pat=re.compile(r'\"(.*)\"')
text1='computer says "no."'
str_pat.findall(text1)
#['no.']
#Drawback of the above code are as follow 
text2='computer says "no." phone says "yes."' 
str_pat.findall(text2)
#Out[34]: ['no." phone says "yes.']
# we can solve this drawback as follwos by using the '?' in the pattern
str_pat=re.compile(r'\"(.*?)\"')
str_pat.findall(text2)

#############################3
## extraxct from comment
comment=re.compile(r'/\*(.*?)\*/')
text1='/* this is the comment'
comment.findall(text1)

text2='''/*this is a multiline comment/*'''
comment.findall(text2)
# error are occure
comment=re.compile(r'/\*(.*?)\*/')
