# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:05:58 2024

@author: suraj
"""


#functin isde the function using the case speciific
import re
import nltk
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():     #first letter of the text capital 
            return word.capitalize()
        else:
            return word
    return replace
text='UPPER PYTHON,lower python,Mixed Python'
re.sub('python', matchcase('snake'),text,flags=re.IGNORECASE)

'''re.sub('python', matchcase('snake'),text,flags=re.IGNORECASE)
Out[7]: 'UPPER SNAKE,lower snake,Mixed Snake'''
# it concatenate the string at the last of the string

#################
#exttract the text from the comment
# ie in the double quote or the single qoutu
str_pat=re.compile(r'\"(.*)\"')
text1='Computer say "no."'
str_pat.findall(text1)
'''Out[15]: ['no.']
it can extract only the commented part
the single quote and double quote are callled delimetr'''
##
#drwaback
text2='Computer say "no," phone say"yes."'
str_pat.findall(text2)
'''ut[16]: ['no," phone say"yes.']
it give  the extra part
we want only the commente d the part
so ues the following pattern'''
str_pat=re.compile(r'\"(.*?)\"')
str_pat.findall(text2)
'''Out[17]: ['no,', 'yes.']
the drawback are solve by uing the ? mark'''
###################
# the part are return in the multiline comment then use the following pattern
comment=re.compile(r'/\*(.*?)\*/')
text1='/* this the comment*/'
comment.findall(text1)
'''Out[18]: [' this the comment']'''
#############3

text2='''/* this the 
            multiline comment
            you can use it in ttthe proper way*/'''
comment.findall(text2)
#get the empty list
# this the problem of the upper pattern 
#so you can use the below pattern also
#you want to fix the problem you can add the newline to the pattern
comment=re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)
'''Out[21]: [' this the \n            multiline comment']
you will get the proper output'''
#write the all the pattern  in the notebook


'''----------------------2.30------------------------------------'''
#removing  the number from  the text
import  re
def remove_number(text):
    result=re.sub(r'\d+','',text)
    return result
input_str=" There are 3 balls in this bag.and 12 in the bucket"
remove_number(input_str)
"""Out[4]: ' There are  balls in this bag.and  in the bucket'
all the numnre are removecd"""

##############################
# number can converted into the text(letter)/words
#convertting the nuber into the code(text)
#import the package inflect libarary
import inflect
p=inflect.engine()# p is used to infect the engine

#convert  the number into the words
def convert_number(text):
    #spilte the numbrevin tie the string
    temp_str=text.split()
    #initialise the empty list
    new_string=[]
    for word in temp_str:
        #if the word is the digit convert the digits
        #to the nuners and append into the new_string list
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
        #append the word as it is
        else:
            new_string.append(word)
        #join the words of the new_string to the a string
        temp_str=' '.join(new_string)
    return temp_str
input_str=" There are 3 balls in this bag.and 12 in the bucket"
convert_number(input_str)
'''Out[13]: 'There are three balls in this bag.and twelve in the bucket'''
#in this code we want to write the function defination first
#in that we use the split method to split the text in the list and 
# then check each number into the the list
#in that we can check each lettre into the list and when we get the numbre 
#we can convert that nuber into the letter #
#and again we can convert it into the text 

#####################################
#1) reverse each word from the string incomplete ***********************
def reverseWordSentence(Str):

	words = Str.split(" ")
	
	newWords = [word[::-1] for word in words]
	newSentence = " ".join(newWords)

	return newSentence

Str = 'My Name is jessa'
print(reverseWordSentence(Str))
#yM eman si asseJ
#split()
#resver  each word from the list
#finally we use  join() function to9 the list
##############################################
#2) read text file which is save in the working directory
#crete the file and wrote the each word in the new line
file_name='sample.txt'
with open(file_name,'r') as obj:
    cont=obj.read()
print(cont.replace('\n',""))
#####################################################3




















