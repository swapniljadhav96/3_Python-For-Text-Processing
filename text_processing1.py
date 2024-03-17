#Tokenization
txt='welcome to the new year 2023'
x=txt.split()
print(x)
###############################
'''
Removing Special Characters

Special characters, as you know, 
are non-alphanumeric characters. 
These characters are most often found in comments,
 references, currency numbers etc. 
 These characters add no value to text-understanding
 and induce noise into algorithms.
 For that regex package is used

'''
# imports
import re# function to remove special characters
def remove_special_characters(text):
    # define the pattern to keep
    pat = r'[^a-zA-z0-9.,!?/:;\"\'\s]' 
    return re.sub(pat, '', text)
 
# call function
remove_special_characters("007 Not sure@ if this % was #fun! 558923 What do# you think** of it.? $500USD!")
#############################################
#Removing Numbers
'''
As you saw above, the text is retained. 
But sometimes these might not be required. 
Since we are dealing with text, 
so the number might not add much information 
to text processing. So, numbers can be removed 
from text. We can use regular-expressions (regex) 
to get rid of numbers.
 This step can be combined with above one 
 to achieve in single step.
'''
# imports
import re# function to remove numbers
def remove_numbers(text):
    # define the pattern to keep
    pattern = r'[^a-zA-z.,!?/:;\"\'\s]' 
    return re.sub(pattern, '', text)
 
# call function
remove_numbers("007 Not sure@ if this % was #fun! 558923 What do# you think** of it.? $500USD!")
#' Not sure if this  was fun!  What do you think of it.? USD!'

txt='welcome: to the, new year; 2023!'
import re
x=re.split(r'(?:,|;|\s)\s*',txt)
print(x)
#################
#Removing Punctuation
'''
This can be clubbed with step of removing 
special characters. Removing punctuation 
is fairly easy. It can be achieved by using 
string.punctuation and keeping everything 
which is not in this list.

'''
# imports
import string# function to remove punctuation
def remove_punctuation(text):
    text = ''.join([c for c in text if c not in string.punctuation])
    return text# call function
remove_punctuation('Article: @First sentence of some, {important} article having lot of ~ punctuations. And another one;!')
###########################################
#Stemming
#Stemming is the process of reducing 
#inflected/derived words to their word stem, 
#base or root form
#These mainly rely on chopping-off ‘s’, ‘es’, ‘ed’, 
#‘ing’, ‘ly’ etc from the end of the words 
#and sometimes the conversion is not desirable. 
#But nonetheless, stemming helps us in standardizing text.

# imports
import nltk# function for stemming
def get_stem(text):
    stemmer = nltk.porter.PorterStemmer()
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    return text# call function
get_stem("we are eating and swimming ; we have been eating and swimming ; he eats and swims ; he ate and swam ")
##################################################
'''
Though stemming and lemmatization both generate the root form 
of inflected/desired words, but lemmatization is an advanced 
form of stemming. Stemming might not result in actual word, 
whereas lemmatization does conversion properly with the use of vocabulary
'''

line = 'asdf fjdk; afed, fjek,asdf, foo'

re.split(r'(?:,|;|\s)\s*', line)
######################################
pattern=r'(?:,|;|\s)\s*'
x=re.split(pattern,txt)
print(x)
####################################
#matching text at the start or end of string
filename='spam.txt'
filename.endswith('.txt')
#################
area_name='6 th lane west Andheri'
area_name.endswith('west Andheri')
##################################
choices=('http:','ftp:')
url='http://www.python.org'
url.startswith(choices)
#############################
#Slicing a String
#If S is a string, the expression S [ start : stop : step ] 
#returns the portion of the string from index start to index stop, 
#at a step size step.
S = 'ABCDEFGHI'
print(S[2:7])	# CDEFG
#Note that the item at index 7 'H' is not included.
#Slice with Negative Indices
S = 'ABCDEFGHI'
print(S[-7:-2])
#CDEFG
#Slice with Positive & Negative Indices
S = 'ABCDEFGHI'
print(S[2:-5])	# CD
#Specify Step of the Slicing
#You can specify the step of the slicing using step parameter. 
#The step parameter is optional and by default 1.
# Return every 2nd item between position 2 to 7
S = 'ABCDEFGHI'
print(S[2:7:2])	# CEG
# Returns every 2nd item between position 6 to 1 in reverse order
S = 'ABCDEFGHI'
print(S[6:1:-2])
#Slice at Beginning & End
#Omitting the start index starts the slice from the index 0.
# Meaning, S[:stop] is equivalent to S[0:stop]
####################################################
# Slice first three characters from the string
S = 'ABCDEFGHI'
print(S[:3])    # ABC
#Whereas, omitting the stop index extends the slice 
#to the end of the string. Meaning, S[start:] is equivalent to 
#S[start:len(S)]
#######################################################
# Slice last three characters from the string
S = 'ABCDEFGHI'
print(S[6:]) 
#GHI
#########################################################3
#Reverse a String
#You can reverse a string by omitting both start and stop indices 
#and specifying a step as -1.
S = 'ABCDEFGHI'
print(S[::-1])    # IHGFEDCBA
#########################################
#similar operations can be done with slices
filename='spam.txt'
filename[-4:]=='.txt'
#########################
url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'
##########################
from fnmatch import fnmatch,fnmatchcase
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]
#['Dat1.csv', 'Dat2.csv']
##################################
from fnmatch import fnmatch,fnmatchcase
names = ['Andheri East', 'Parle East','Dadar West']
[name for name in names if fnmatch(name, '* East')]
#['Andheri East', 'Parle East']
####################################

addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]
#You could write list comprehensions like this:
from fnmatch import fnmatchcase
[addr for addr in addresses if fnmatchcase(addr, '* ST')]
################################################
text = 'yeah, but no, but yeah, but no, but yeah'
 # Exact match
text == 'yeah'
#False
# Match at start or end
text.startswith('yeah')
#True
text.endswith('no')
#False

# Search for the location of the first occurrence
text.find('no')
#10
########################################
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
#yes
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
#no
################################
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat, text1):
    print('yes')
else:
    print('no')
 #yes   
if re.match(datepat, text2):
    print('yes')
else:
    print('no')
    #no
    ######################################
    #Searching and replacing text
text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep')
##############################################
#if you have dates in format 11/27/2012 want to convert 2012-11-27
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)#\3 3 rd group,\1 st group
#'Today is 2012-11-27. PyCon starts 2013-3-13.'
##########################################
#if you want to know how many substitutions are made in text then
#you can use subn() method
newtext, n = datepat.subn(r'\3-\1-\2', text)
newtext
#####################################################
text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
#to substitute
re.sub('python', 'snake', text, flags=re.IGNORECASE)
#'UPPER snake, lower snake, Mixed snake'
######################################################
#The last example reveals a limitation that 
#replacing text won’t match the case of the
#matched text. If you need to fix this, 
#you might have to use a support function, as in the
#following:
import re
def matchcase(word):
     def replace(m):
        text = m.group()
        if text.isupper():
           return word.upper()
        elif text.islower():
             return word.lower()
        elif text[0].isupper():
             return word.capitalize()
        else:
             return word
     return replace
re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
##############################
#You’re trying to match a text pattern using regular expressions, 
#but it is identifying the
#longest possible matches of a pattern. 
#Instead, you would like to change it to find the
#shortest possible match.
#This problem often arises in patterns 
#that try to match text enclosed inside a pair of
#starting and ending delimiters (e.g., a quoted string). 
#To illustrate, consider this example:
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1)
#['no.']
#However if we have text as below
text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2)
#['no." Phone says "yes.']
#In this example, the pattern r'\"(.*)\"' 
#is attempting to match text enclosed inside
#quotes. However, the * operator in a regular expression 
#is greedy, so matching is based
#on finding the longest possible match
str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)
##############################
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
comment.findall(text1)
#[' this is a comment ']
text2 = '''/* this is a
            multiline comment */
 '''
comment.findall(text2)
#To fix the problem, you can add support for newlines.
# For example:
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
#In this pattern (?:.|\n) specifies a capture group
#i.e.it defines the group of purpose of matching
#but that group is not captured seperately
comment.findall(text2)
#[' this is a\n            multiline comment ']

#There is another option which addresses this problem
#The re.compile() function accepts a flag, re.DOTALL, which is useful here. It makes
#the . in a regular expression match all characters, including newlines. For example:
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
comment.findall(text2)
##################################################
#Normalizing Unicode text to standard represenation
#You’re working with Unicode strings, but need to make sure 
#that all of the strings have
#the same underlying representation.
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
s1==s2
#False


import unicodedata
t1 = unicodedata.normalize('NFC', s1) #Normalization form of canonical composition
t2 = unicodedata.normalize('NFC', s2)
t1 == t2
#True
print(ascii(t1))
#'Spicy Jalape\xf1o'
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
t3 == t4
#True
print(ascii(t3))
#'Spicy Jalapen\u0303o'

#Normalization is an important part of any code that needs to ensure that it processes
#Unicode text in a sane and consistent way. This is especially true when processing strings
#received as part of user input where you have little control of the encoding.
#Normalization can also be an important part of sanitizing and filtering text.

t1 = unicodedata.normalize('NFD', s1)
''.join(c for c in t1 if not unicodedata.combining(c))
#'Spicy Jalapeno'
#####################################################
#Working with Unicode Characters in Regular #Expressions
#You are using regular expressions to process text, but are concerned about the handling
#of Unicode characters.
import re
num = re.compile('\d+')
# ASCII digits
num.match('123')
#<re.Match object; span=(0, 3), match='123'>

#it’s also important to be aware of special cases. For example, consider the behavior of caseinsensitive
#matching combined with case folding:
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s) # Matches
#<re.Match object; span=(0, 6), match='straße'>
pat.match(s.upper()) # Doesn't match
s.upper() # Case folds
#'STRASSE'
#############################################
#Stripping Unwanted Characters from Strings
#You want to strip unwanted characters, such as whitespace, from the beginning, end, or
#middle of a text string.
#The strip() method can be used to strip characters from the beginning or end of a
#string. lstrip() and rstrip() perform stripping from the left or right side, respectively.
#By default, these methods strip whitespace
 # Whitespace stripping
s = '   hello world   \n'
s.strip()
#'hello world'
s = '   hello world   \n'
s.lstrip()
#'hello world \n'
s = '   hello world   \n'
s.rstrip()
s = '   hello world   \n'
#' hello world'

 # Character stripping
t = '-----hello====='
t.lstrip('-')
#'hello====='
t = '-----hello====='
t.strip('-=')
#'hello'


s = ' hello world       \n'
s = s.strip()
s
#'hello world'

s.replace(' ', '')
#'helloworld'
import re
re.sub('\s+', ' ', s)
'hello world'
###########################################


s = 'pýtĥöñ\fis\tawesome\r\n'
s
#'pýtĥöñ\x0cis\tawesome\r\n'

#The first step is to clean up the whitespace. To do this, 
#make a small translation table
#and use translate():
remap = {
     ord('\t') : ' ',
     ord('\f') : ' ',
     ord('\r') : None # Deleted
}
a = s.translate(remap)
a
#####################################
#As you can see here, whitespace characters such as \t and \f have 
#been remapped to a
#single space. The carriage return \r has been deleted entirely.
#You can take this remapping idea a step further and build 
#much bigger tables. For example,
#let’s remove all combining characters:

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) 
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
b
#'pýtĥöñ is awesome\n'
b.translate(cmb_chrs)
#'python is awesome\n'
#Yet another technique for cleaning up text 
#involves I/O decoding and encoding functions.
#The idea here is to first do some preliminary 
#cleanup of the text, and then run it
#through a combination of encode() or decode() operations
# to strip or alter it.
a='pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD', a)
b.encode('ascii', 'ignore').decode('ascii')
#'python is awesome\n'

###########################################
#Aligning the text string
text = 'Hello World'
text.ljust(20)
#'Hello World '
text.rjust(20)
#' Hello World'
text.center(20)
#' Hello World '
#################################
#All of these methods accept an optional characters &fill character as well. For example:
text.rjust(20,'=')
#'=========Hello World'
text.center(20,'*')
#'****Hello World*****'
################################
format(text, '>20')#> ->text will be shifted to right side for mentioned spaces
#' Hello World'
format(text, '<20')#<->text will be shifted to left side for mentioned spaces
#'Hello World '
format(text, '^20')
#' Hello World '
#Here you can add charcters to fill the space at left,right or center
#as above but If you want to include a fill character other than a space, specify it before the alignment
#character:
format(text, '=>20s')
#'=========Hello World'
format(text, '*^20s')
'****Hello World*****'

#These format codes can also be used in the format() method when formatting multiple
#values. For example:
'{:>10s} {:>10s}'.format('Hello', 'World')
#'     Hello      World'

#One benefit of format() is that it is not specific to strings. It works with any value,
#making it more general purpose. For instance, you can use it with numbers:
x = 1.2345
format(x, '>10')
#' 1.2345'
format(x, '^10.2f')
#' 1.23
###############################
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)
'Is Chicago Not Chicago?'
','.join(parts)
'Is,Chicago,Not,Chicago?'
''.join(parts)
'IsChicagoNotChicago?'
#########################
#if you join very few strings then you can use + operator
a = 'Is Chicago'
b = 'Not Chicago?'
a + ' ' + b
#'Is Chicago Not Chicago?'
#####################
print('{} {}'.format(a,b))
#Is Chicago Not Chicago?
print(a + ' ' + b)
#Is Chicago Not Chicago?
##############################
a='Hello' 'world'
a
##################
a='Hello'' ' 'world'
a
####################

#Interpolating Variables in Strings
#You want to create a string in which embedded variable names are substituted with a
#string representation of a variable’s value.
s = '{name} has {n} messages.'
s.format(name='Guido', n=37)
######################################
name = 'Guido'
n = 37
s.format_map(vars())
#'Guido has 37 messages.'
#######################
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
#Here’s how you can use the textwrap module to reformat it in various ways:
import textwrap
print(textwrap.fill(s, 70))
'''
Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
not around the eyes, don't look around the eyes, look into my eyes,
you're under.
'''

print(textwrap.fill(s, 40))
'''
Look into my eyes, look into my eyes,
the eyes, the eyes, the eyes, not around
the eyes, don't look around the eyes,
look into my eyes, you're under.

'''

print(textwrap.fill(s, 40, initial_indent=' '))
'''
   Look into my eyes, look into my eyes,
the eyes, the eyes, the eyes, not around
the eyes, don't look around the eyes,
look into my eyes, you're under.

'''
print(textwrap.fill(s, 40, subsequent_indent=' '))
'''
Look into my eyes, look into my eyes,
 the eyes, the eyes, the eyes, not
 around the eyes, don't look around the
 eyes, look into my eyes, you're under.

'''
##############################################


#######################################

import nltk
sentence_data = "The First sentence is about Python. The Second: about Django. You can learn Python,Django and Data Ananlysis here. "
nltk_tokens = nltk.sent_tokenize(sentence_data)
print (nltk_tokens)
############################
#Non-English Tokenization
import nltk

german_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens=german_tokenizer.tokenize('Wie geht es Ihnen?  Gut, danke.')
print(german_tokens)
#################################
#word tokenization
import nltk

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print (nltk_tokens)
#################################
import nltk
nltk.download('stopwords')
#It will download a file with English stopwords.
#Verifying the Stopwords

from nltk.corpus import stopwords
stopwords.words('english')
#The various language other than English which has these stopwords are as below.

from nltk.corpus import stopwords
print (stopwords.fileids())
######################################
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))

all_words = ['There', 'is', 'a', 'tree','near','the','river']
for word in all_words: 
    if word not in en_stops:
        print(word)
##################################
import nltk
nltk.download('omw-1.4')
from nltk.corpus import wordnet

synonyms = []

for syn in wordnet.synsets("Soil"):
    for lm in syn.lemmas():
             synonyms.append(lm.name())
print (set(synonyms))
############################
from nltk.corpus import wordnet
antonyms = []

for syn in wordnet.synsets("ahead"):
    for lm in syn.lemmas():
        if lm.antonyms():
            antonyms.append(lm.antonyms()[0].name())

print(set(antonyms))
####################################
import nltk
word_data = "The Sky is blue also the ocean is blue also Rainbow has a blue colour." 

# First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)

# Applying Set
no_order = list(set(nltk_tokens))

print(no_order)
#######################################
import nltk
word_data = "The Sky is blue also the ocean is blue also Rainbow has a blue colour." 
# First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)

ordered_tokens = set()
result = []
for word in nltk_tokens:
    if word not in ordered_tokens:
        ordered_tokens.add(word)
        result.append(word)
     
print (result) 
##############################################
#To extract emails form text, we can take of regular expression.
# In the below example we take help of the regular expression package to define the pattern of an email ID and then use the findall() function to retrieve those text which match this pattern.

import re
text = "Please contact us at contact@xyz.com for further information."+\
        " You can also give feedbacl at feedback@xyz.com"


emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print (emails)
###########################################
#We can take a input file containig some URLs and process it 
#thorugh the following program to extract the URLs. The findall()function is used to find all instances matching with the regular expression. 
import re
 
with open("c:/10-python/url.txt") as file:
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            print(urls)
#####################################
#Capitalization strings is a regular need in any text processing system. Python achieves it by using the built-in functions in the standard library. In the below example we use the two string functions, 
#capwords() and upper() to achieve this. 
import string

text = 'Machine learning - advanced technology to learn'

print (string.capwords(text))
print (text.upper())
###########################################
#Translation in python essentially means substituting specific letters with another letter. It can work for encryption decryption of strings.
import string

text = 'Machine learning - advanced technology to learn'

transtable = text.maketrans('chd', 'abc')
print (text.translate(transtable))
#############################

#Using regular expressions there are two fundamental operations which appear similar but have significant differences. The re.match() checks for a match only at the beginning of the string, while re.search() checks for a match anywhere in the string.

import re

if  re.search("tor", "Tutorial"):
        print ("1. search result found anywhere in the string")
        
if re.match("Tut", "Tutorial"):
         print ("2. Match with beginning of string" )
         
if not re.match("tor", "Tutorial"):
        print ("3. No match with match if not beginning" )
#################################################
import re

"""We create a re.MatchObject and store it in
   match_object variable
   the '()' parenthesis are used to define a
   specific group
  """
match_object = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@gmail.com')
""" w in above pattern stands for alphabetical character
    + is used to match a consecutive set of characters
    satisfying a given condition
    so w+ will match a consecutive set of alphabetical characters"""
# for entire match
print(match_object.group())
# also print(match_object.group(0)) can be used

# for the first parenthesized subgroup
print(match_object.group(1))

# for the second parenthesized subgroup
print(match_object.group(2))

# for the third parenthesized subgroup
print(match_object.group(3))

# for a tuple of all matched subgroups
print(match_object.group(1, 2, 3))
##############################################
import random

import re

def replace(t):
    inner_word = list(t.group(2))
    random.shuffle(inner_word)
    return t.group(1) + "".join(inner_word) + t.group(3)
text = "Hello, You should reach the finish line."
print( re.sub(r"(\w)(\w+)(\w)", replace, text))

print (re.sub(r"(\w)(\w+)(\w)", replace, text))
#####################################
#Replacing the complete string or a part of string is a very frequent
# requirement in text processing. The replace() method returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to max.
str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
##############################
#Replacement Ignoring Case
import re
sourceline  = re.compile("Tutor", re.IGNORECASE)
 
Replacedline  = sourceline.sub("Tutor","Tutorialspoint has the best tutorials for learning.")
print (Replacedline)
#############################
#pip install pyspellchecker
from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(['let', 'us', 'wlak','on','the','groun'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))
# Get a list of `likely` options
    print(spell.candidates(word))
##################################

