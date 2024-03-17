# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:03:22 2024

@author: suraj
"""


'''-----------------python for text processsing---------------------'''
# how to use python for nlp
# text processing
# data science :1nlp,2 visualization,3reinforcemen
#NLP is imp
#NLP#
#tokenization:- spliting the senetnce in the word
txt='welcome to the new year 2023'
x=txt.split()
print(x)
'''print(x)
['welcome', 'to', 'the', 'new', 'year', '2023']'''


###############################
'''removing the special character use the re package
^ accept all
the speciall caharatcetre do not have any value
in this we can filtetr all the special character by using the r'
'''
import re# function to remove special charater
def remove_special_char(text):
    #define the pattern keep
    pat=r'[^a-zA-z0-9.,!?/:;\"\'\swas]'# except this all are come:r''
    return re.sub(pat, ' ' ,text)
#call the function
remove_special_char('007 Not sure@$ th\is was./ the! "good for the^& health')
#accept all ^
#it can remove the all the unnessacary data or specailal charater are that was not usefull for the texr
#we can remove that the data by using the 're' package and it can retrun only the useful data or the text
########################################

#removing the number
'''as u '''

import re # function to remove special charater
def remove_special_char(text):
    #define the pattern keep
    pat=r'[^a-zA-z.,!?/:;\"\'\swas]'# except this all are come
    return re.sub(pat, ' ' ,text)
#call the function
remove_special_char('007 Not sure@$ th\is was./ the! "good  243 for the^& health')
'''Out[17]: '    Not sure   th\\is was./ the! "good      for the^  health'''
#pat it has element we can remove the elemnt which was not belong to the pat
##########################
# remove or split ont the text as (like the pattern as list)
txt='welcome:to the ,new year;2023!'
import re
x=re.split(r'(?:,|;|\s)\s*',txt)
print(x)

###################################
#remove the punction function:- it can concatatnate the string multiple
'''this can be clubbed with step of removing special charater Removing the punction'
'''
#''.join is ued to concatanation of the charater or sysmbol
#import
import string # function to remove the punction
def remove_punctuation(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text# call the function
remove_punctuation('Artical: @% iris sentence ,{important} artical.')
#list comprehension
'''remove_punctuation('Artical: @% iris sentence ,{important} artical.')
Out[21]: 'Artical  iris sentence important artical'''
# in the above example we can remove all the punctuation mark present in the text
###########################




'''--------------------------------------------------------------------'''
# preprocessing
#stemming :- use nltk package
# get the dataset then do the folling procee on the data set
# septrate out sentance
#seprate the word
#remove punction mark
# removespecila charetet
#eg
#going:-go,eating:-eat 
#it all called streming
#stremming
'''write information of the stremming'''
import nltk# function of stremming
def get_stem(text):
    stemmer=nltk.porter.PorterStemmer()
    text=''.join([stemmer.stem(word) for word in text.split()])
    return text
print(get_stem("this is eating and swining  ; we have going to platy ; this is the greated thing"))
'''Out[7]: 'thiiseatandswine;wehavegotoplati;thiisthegreatthing'''
# it can remove the extre word which you can add for the verb in the sentence and it can concetenate the multiple string in the same statment
####################################################
#lemmatization :- it is the advanced form of the stemming next study
# '^ 'except the this all are filter out
line='asdf fjdk ; fjek,asdf , foo'

re.split(r'(?:,|;|\s)\s*',line)
#except all the above metion statement  we can remove or split  extra word or all the  word  
'''Out[15]: ['asdf', 'fjdk', '', 'fjek', 'asdf', '', 'foo']'''
####################################33
#
pattern=r'(/:,|;|\s)\s*'
x==re.split(pattern.txt)
print(x)
###############################
#matching the text at the start or end of the string
filename='span.txt'
filename.endswith('.txt')
'''filename.endswith('.txt')
Out[19]: True'''
#it can make matches with the  enetr file name and endswith text
###################################
# use cases
area_name='6 th lane west andheri'
area_name.endswith('west andheri')
'''area_name.endswith('west andheri')
Out[21]: True'''
# it is present in the string
#####################################
#endswith and statswith are provided under nltk
choice=('http:','ftp:')
url1='http://www.phython.org'
url1.startswith(choice)


###################################
#slice the string
#sytanx string[start:end:step]
#
s='ASDFGHJKUYTR'
print(s[2:7])   #DFGHJ
#note the thing that is the last index value are not include in the output statemenet
########################################
#slicing with the negative index
s='ASDFGHJKUYTR'
print(s[-7:-2]) #HJKUY
# in the negative index the it not take the last index but it take the first index
############################33
##slice the positive and negative number
s='ASDFGHJKUYTR'
print(s[2:-5])
#DFGHJ
#it can take last negative index valuei.e it take the value infront of him

#######################################
#specify step of the slice
s='ASDFGHJKUYTR'
print(s[2:7:2]) #DGJ

###########################
# it give the negative step also
s='ASDFGHJKUYTR'
print(s[6:1:-2])
#JGD
########################
#slice 1st three chater from string
s='ASDFGHJKUYTR'
print(s[:7])
##############################
#slice 3 charater from string
s='ASDFGHJKUYTR'
print(s[6:])
###############################
 #reveres string
s='ASDFGHJKUYTR'
print(s[::-1])
#################################
##smilare opertaiom can be done with slices  on the dataset
filename='span.txt'
filename[-4:]=='.txt'

'''Out[30]: '.txt'''
#true
############################
#check the otr compare with index value and text in the string 
url1='http://www.phython.org'
url1[:5]=='http:'

#Out[31]: True
