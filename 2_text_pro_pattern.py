# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:04:36 2024

@author: suraj
"""

#fnmatch,fnmatchcase:-use to perform search matchinng
from fnmatch  import fnmatch ,fnmatchcase
names=['Dat1.csv','Dat2.csv','config.int','foo.csv',]
[name for name in names if fnmatch(name,'Dat*.csv')]#list comprehension
#Out[3]: ['Dat1.csv', 'Dat2.csv']
#Dat* means Dat1,Dat2,Dat3 ..etc
###################################3
#fnmatchcase
from  fnmatch import fnmatch,fnmatchcase
names=['Andheri east','dadar east','dhade west']
[name for name in names if fnmatchcase(name,'*east')]
#Out[6]: ['Andheri east', 'dadar east']
#*east it can  match the word which can end with the east
#############################################
#matching in the address
#use case :-it can use in the row material  you want to extra
#the data from the list or the from the dataset then they can use the fnmatch and 
#fnmatchcase
addresses=[
    '5412 N clark st',
    '1060 W addisoin st',
    '1039 W granvill ave', 
    '2121 N clark st',
    '4802 n broadway',]
from fnmatch import fnmatch,fnmatchcase
[addre for addre in addresses if fnmatchcase(addre,'*st')]
#Out[10]: ['5412 N clark st', '1060 W addisoin st', '2121 N clark st']
# it can give the output as the addresses end with the 'st' from the list

########################################################
#try to compare the string hole and operation on the string
text='yeah, but yeah,but yeah, but no ,but yeah'
#exact match
text=='yeah'
#output false
#hhreer the  text is not equl to yeah
###########
#match st start or end
text.endswith('yeah')
#o/p:-true
#string is endswith the yeah
text.endswith('no')
#o/p:- false
# becaue of the string is not end with the no
#search for the location for the first occurance
text.find('no')
#o/p:-29
# it can give first occurance letter index value

###################################
#match the date
#matching with the date with \d+ command
#imp
text1='11/27/2023'
text2='Nov 27,2012'
import re#
#simple matching :-\d+ means match one or more digits
if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')
#o/p:-yes
if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')
#o/p:- no
###################################3
###regular expression called regex are descripted for the pattern of the text
text='23-11-2023'
import re
if re.match(r'\d\d-\d\d-\d\d\d\d',text):
    print('yes')
else:
    print('no')
#yes
#\d\d-\d\d-\d\d\d\d:- 23-11-2023


'''-------------------------------------2.30------------------------------------'''
#assigment
#notes are written in the note book
#spllit by simple method
text= 'this is the artifical era '
x=text.split()
print(x)
'''['this', 'is', 'the', 'artifical', 'era']'''
# in it white space as separater
##############################3
#spliting the word by using re package
text='India: has great history : in 2023 * india is leading to its glowing future!'
import re
x=re.split(r'(?:,|;|\s)\s*',text)
print(x)
#here the separatere are : 
# se
"""['India:', 'has', 'great', 'history', ':', 'in', '2023', 'india', 'is', 'leading', 'to', 'its', 'glowing', 'future!']"""
#in the above example we take  the india: as one word
#################
#here the comma(,) is the separator
text='India, has great history , in 2023 * india is leading to , its glowing future!'
import re
x=re.split(r'(?:,|;|\s)\s*',text)
print(x)
###############################
#matching text at the start or ennd of the string
text='ram went to haridhoor to get the gangjaal'
#check ythe text gangajaal
text.endswith('gangjaal')

'''text.endswith('gangjaal')
Out[29]: True'''

############
#start with
text.startswith('went')
'''Out[30]: False'''

#many word check
choices=['mango','grapes']
text='I  like mango'
#check ythe text mango
text.endswith(choices)
#################
# string slice
#only want mango
text='i like mango '
text[7:]
#o\p:-' mango'

################3
#extrect the only date from thr below statement
text='i have vistiide pune 11/5/2023'
text[21:]
#o\p:-Out[59]: '11/5/2023'
#####*
#or by match fun
text='i have vistiide pune 11/5/2023'
import re
if re.match(r'\d+/\d+/\d+',text):
    print('yes')
else:
    print('no')
    
###################
#searching and replacing text
text='yeah, but yeah,but yeah, but no ,but yeah'
text.replace('yeah','yeap')
#.replace(world;replace word)
#Out[79]: 'yeap, but yeap,but yeap, but no ,but yeap'
###################3
#sub()
text='today is 17/05/2023 and our exam start from 03/07/2023'
import re
re.sub(r'(\d+)/(\d+)/(\d+)',r'(\3-\1-\2)',text)
'''today is (2023-17-05) and our exam start from (2023-03-07)
3 2023
1 05
2 17'''

########################
#using complie method
import re
datepat=re.compile(r'(\d+)/(\d+)/(d+)')
datepat.sub(r'\3-\1-\2',text)
'''Out[88]: 'today is 17/05/2023 and our exam start from 03/07/2023'''
###############################3
#subn():-This function is similar to sub() in all ways except the way in which it provides the output
newtext,n=datepat.subn(r'\3-\1-\2',text)
newtext
n
#Out[89]: 0
##############################
#repalce and searching the teext sensitive text
text='UPPER PYTHON,lower python,Mixed Python'
re.findall('python',text,flags=re.IGNORECASE)
#it can find alll the python word in the text 
#and the flags ignore the word style
re.sub('python','snake',text,flags=re.IGNORECASE)
#it will replace all the python word in the  text
# iit can i.e not take word stystle










