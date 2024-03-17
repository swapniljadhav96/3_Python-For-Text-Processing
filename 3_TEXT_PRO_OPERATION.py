# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:06:52 2024

@author: suraj
"""

'''------------------------------2.30------------------------------------------'''
#unicode:- video and the link
#normalizing the unicode text to standard respretation
#you are working withe r unicode strings but need to make sure
#that all the string have
#the same uderlying representaion

s1='Spicy Jalape\u00f1o'
s2='Spicy Jalapen\u0303o'
print(s1)
print(s2)
s1==s2#o\p:-false 
#in the above exmaple we can see that the encoduing operation perform on the two differnt string 
#which means in differnt format
#they are same in the one language
#s1==s2 are  not same unicode
####################
#to solve this problem use 
#normalization:-procees of converting the code in normalise form
#unicodedata
#NFC
#NFD
import unicodedata
t1= unicodedata.normalize('NFC',s1)#normalization
t2=unicodedata.normalize('NFC',s2)
t1==t2#o/p:- true
################3
#normalization using NFD
print(ascii(t1))
'''Spicy Jalape\xf1o'''#nfc
t3= unicodedata.normalize('NFD',s1)#normalization
t4=unicodedata.normalize('NFD',s2)
print(t3)
print(t4)
t3==t4#true
print(ascii(t3))
'''Spicy Jalapen\u0303o'''#nfd

##############################3
#finding the text in normalization form
#unicodedata.combining() for combing the charaterby charater
t1==unicodedata.normalize('NFD',s1)
''.join(c for c in t1 if not unicodedata.combining(c))
#Out[18]: 'Spicy Jalapẽo''

#####################################
#working with unicode chara in regular #expression
#
import re 
num =re.compile('\d+')
#ascii digits
num.match('123')
#<re.match object; span=(0,3),match='123'>
#it
pat=re.compile('Stra\u00dfe',re.IGNORECASE)
pat
s='straße'
pat.match(s) #matches

pat.match(s.upper())



######################
#stripping the unwanted charater from string
#by default  this method strip whitspace
#whitespace stripping
s='    hello world     \n'
s.strip()
'''Out[29]: 'hello world'
'''
######
#without passing the argument to the function
#1).lstrip() :- remove the white space from the left side
s.lstrip()
'''Out[40]: 'hello world     \n'
it can remove the only the left side white space
'''
#2) .rstrip():- remove the white space from the right sde
s.rstrip()
'''Out[41]: '    hello world'
it can remove the only the right side white space'''

###################
#character stripping
#passing the argument for function
t='-----hello======='
#1) .lstrip(arg)
t.lstrip('-')
'''Out[33]: 'hello=======
'
it can remove the only the left side unwanted data'''
#2).rstrip(arg)
t.rstrip('=')
'''Out[33]: '-----hello'
it can remove the only the right side unwanted data
'''
#remove both the symbol
t.strip('-=')
#Out[6]: 'hello'




'''--------------------25/5/23---8.15-- IMP for text---------------------------'''
###################################
s='    hello world     \n'
s=s.strip()
s
#Out[20]: 'hello world'
###################
#remove the whitespace
s.replace(' ','')
#Out[11]: 'helloworld'
#it will remove all the whitespace between the string
################################ 
#remove the white space or extra part using the regex
import re
re.sub('\s+',' ',s)
#Out[17]: 'hello world'
###################
#clean the ttext 
s = 'pýtĥöñ\fis\tawesome\r\n'
s   # Out[25]: 'pýtĥöñ\x0cis\tawesome\r\n' it willl show theascii value

################33
s = 'pýtĥöñ\fis\tawesome\r\n'
#the first step is to clean up the white space 
#to do this make the a small translate
#and use the translate():- it can translate the charater into the another lettre
#make the dictory which you want to remove
remap={
       ord('\t') : ' ',
       ord('\f') : ' ',
       ord('\r') : None # delete
       }
a=s.translate(remap)
a
#Out[29]: 'pýtĥöñ is awesome\n'
#remove the \n use the repalce or you can intialize them into the dictonrary
a.replace('\n',' ')
#Out[31]: 'pýtĥöñ is awesome '
#####################
#above text s can be clean by using the unicodedata and sys
#lets remove all combinig charatere
import unicodedata
import sys
cmb_chrs= dict.fromkeys( c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b=unicodedata.normalize('NFD', a)
b
#Out[36]: 'pýtĥöñ is awesome\n'
#clean all the data in the above comment
b.translate(cmb_chrs)
#Out[37]: 'python is awesome\n'
#######################333
#anotter teq for clean the text
#yet another techq for cleaning  up text involves I/O decoding and encoding functions
#the idea share is to first do some prilimnary cleanup  of the text And then run it 
#through combination the encode( ) or decode() opertion to strip or alter it
a='pýtĥöñ is awesome\n'
b=unicodedata.normalize('NFD',a)
b.encode('ascii','ignore').decode('ascii')
#Out[40]: 'python is awesome\n'
#frist up all we can make the text in the 
#normalization decode form
#and then perform that operation are below 
#in the above text we first make the text in the encode form and 
#ignore that  encode form and decode that ascii value which will bwe
#made by the encode and write that decode form  


################################3
#aligning  of the text right and left and center
text='Hello world'
#left align
text.ljust(20)
#Out[43]: 'Hello world         ' 20 white space are generated by the left side
#right aligen
text.rjust(20)
#Out[44]: '         Hello world' 20 white space are genertaed ao the right side
#center align
text.center(20)
# Out[45]: '    Hello world     ' 10 left and 10 right space
###########################
#fill the white space with the symbol in the align
text.rjust(20,'=')
#Out[46]: '=========Hello world'
text.ljust(20,'=')
#Out[47]: 'Hello world========='
text.center(20,'*')
#Out[48]: '****Hello world*****'
##############################
#shiftinng of the text by uisng the arrow'>,<,^
format(text,'>20')
#Out[49]: '         Hello world' it >  can shift the text to left side
format(text,'<20')
#Out[50]: 'Hello world         'it <  can shift the text to right side
format(text,'^20')
#Out[51]: '    Hello world     '
##################################
#here you can add charater to fill the space at left right center
#as above but if want to include a fill charater other than a space
#chareater

format(text,'=>20s')
#Out[53]: '=========Hello world'left
format(text,'*^20s')
#Out[54]: '****Hello world*****' center

#####################################
# these formate codes can also be used in the format() methode when formatting the value
'{:>10s} {:>10s}'.format('Hello',' world')
#Out[56]: '     Hello      world'
#first hello world shifted  10 space to the left and from  that 10 space  from thr left from the hello 





"""------------------------------2.50--25/5/23--------------------"""
#one benefit of the format() is that it is mot specific to string
#making
x=1.2345
format(x,'>10')
#Out[4]: '    1.2345'
x
format(x,'^10.2f')
#Out[7]: '   1.23   '


###############################
#concatetanate the list to the string are following method
parts=['Is','Chicago','Not',' Chicago?']
' '.join(parts)
#Out[9]: 'Is Chicago Not  Chicago?'
########
#separaet teh text by using the comma
','.join(parts)
#Out[10]: 'Is,Chicago,Not, Chicago?'
##########
#join rhe list withou the white space
''.join(parts)
#Out[11]: 'IsChicagoNot Chicago?'

#####################################
#if you join very few strings then you can se the + opertator
a='Is Chicago'
b=' Not Chicago?'
a+' '+b             #
#Out[14]: 'Is Chicago  Not Chicago?'
###################################
#use .format() is helpful in the large amout of the string are given
print('{} {}'.format(a,b))
#o/p:-Is Chicago  Not Chicago?
###################################
#another method to join the two string 
print(a+' '+b)
#o/p:-Is Chicago  Not Chicago?
############################################
#when ther is no given any concatetion operator are not given that time
a='Hello' 'world'
a

###########################33
##
a='Hello'' ''World'
a

###################################################
#interpolating variable in string
#you want to ccreate a string in which embedded variable names
#string represtation of the variables value

s='{name} has {n} messages'
s.format(name='Guido',n=37)
#Out[18]: 'Guido has 37 messages'

##############################################
#if are changing the pposutuin then it can show the differnt result
s='{name} has {n} messages'
name='Guido'
n=37
s.format_map(vars())
#Out[22]: 'Guido has 37 messages'

#######################################3
#rearrnge the text
#indentation
#textwrapping  using textwrap
s = ' Look into my eyes,look into my eyes,the eyes ,the eyes,\
Lok into my eyes,look into my eyes,the eyes ,the eyes,\
Look into my eyes,look into my eyes,the eyes ,the eyes,\
Lok into my eyes,look into my eyes,the eyes ,the eyes,'
import textwrap
print(textwrap.fill(s,70))



#################################
#intial indentaion of the text
s
print(textwrap.fill(s,40,intial_indent='   '))

######################################################
#subsequent indenation
print(textwrap.fill(s,40,subsequent_indent=''))