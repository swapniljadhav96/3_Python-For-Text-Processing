# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:11:05 2024

@author: suraj
"""
"""--------------------------Tokenization-----------------------------------------"""
#tokenization
#1)sentance
#2)word
#1) sentence tokenization
import nltk
nltk.download('punkt')
sentence_data="The first sentence is aboout the python. The second sentace tell about the c+"
nltk_tokens=nltk.sent_tokenize(sentence_data)
print(nltk_tokens)
#it can seprate the two sentennce
#['The first sentence is aboout the python.', 'The second sentace tell about the c+']
##########################################3
#non english tokenization'
import nltk
german_tokenizer=nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens=german_tokenizer.tokenize('wie geht es Ihnen? Gut,danke.')
print(german_tokens)

############################################
#word tokenization:- it will split the word from the sentence or the dataframe
#or from  the data set
import nltk
word_data="It origenated from the idea that there are readrers who prefere the the languange"
nltk_tokens=nltk.word_tokenize(word_data)
print(nltk_tokens)
#['It', 'origenated', 'from', 'the', 'idea', 'that', 'there', 'are', 'readrers', 'who', 'prefere', 'the', 'the', 'languange']
##############################################################
#remove the stopwords
#nltk.download('stopwords')
import nltk
nltk.download('stopwords')
#it will download a file with english stopwords
#verififying the stopwords
from nltk.corpus import stopwords
stopwords.words('english')
#the various lang other than english which has this stopwords are as that 
'''['i',
 'me',
 'my',
 'myself',
 'we',
 'our',
 'ours',
 'ourselves',
 'you',
 "you're",
 "you've",
 "you'll",
 "you'd",
 'your',
 'yours',
 'yourself',
 'yourselves',
 'he',
 'him',
 'his',
 'himself',
 'she',
 "she's",
 'her',
 'hers',
 'herself',
 'it',
 "it's",
 'its',
 'itself',
 'they',
 'them',
 'their',
 'theirs',
 'themselves',
 'what',
 'which',
 'who',
 'whom',
 'this',
 'that',
 "that'll",
 'these',
 'those',
 'am',
 'is',
 'are',
 'was',
 'were',
 'be',
 'been',
 'being',
 'have',
 'has',
 'had',
 'having',
 'do',
 'does',
 'did',
 'doing',
 'a',
 'an',
 'the',
 'and',
 'but',
 'if',
 'or',
 'because',
 'as',
 'until',
 'while',
 'of',
 'at',
 'by',
 'for',
 'with',
 'about',
 'against',
 'between',
 'into',
 'through',
 'during',
 'before',
 'after',
 'above',
 'below',
 'to',
 'from',
 'up',
 'down',
 'in',
 'out',
 'on',
 'off',
 'over',
 'under',
 'again',
 'further',
 'then',
 'once',
 'here',
 'there',
 'when',
 'where',
 'why',
 'how',
 'all',
 'any',
 'both',
 'each',
 'few',
 'more',
 'most',
 'other',
 'some',
 'such',
 'no',
 'nor',
 'not',
 'only',
 'own',
 'same',
 'so',
 'than',
 'too',
 'very',
 's',
 't',
 'can',
 'will',
 'just',
 'don',
 "don't",
 'should',
 "should've",
 'now',
 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn',
 "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't",
 'haven', "haven't", 'isn', "isn't", 'ma',
 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]'''

##########################33
#
from nltk.corpus import stopwords
print(stopwords.fields())
#######################################
#remove the stopwords from the sentence
#defination of the stopwordss
from nltk.corpus import stopwords
en_stops=set(stopwords.words('english'))

#remove the stowords
all_words=['There','is','a','tree','near','the','river']
for word in all_words:
    if word not in en_stops:
        print(word)

'''There
tree
near
river'''
#it will remove all the stopwords and only dispaly the unn stopwords

####################################################
#synonyms 
#donload all the word:-nltk.download('omw-1.4')
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
from nltk.corpus import wordnet
#compuslary
synonyms=[]
for syn in wordnet.synsets("Soil"):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print(set(synonyms))
'''
{'territory', 'stain', 'filth', 'grunge', 'colly', 'soil', 'dirty', 'bemire', 'grime', 'grease', 'ground', 'begrime', 'dirt', 'land'}'''
#it give all  synonyms word related to the  soil whic is present in the wordnet
###############################3
#antonyms
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
from nltk.corpus import wordnet
antonyms=[]
for syn in wordnet.synsets("ahead"):
    for lm in syn.lemmas():
        if lm.antonyms():
            antonyms.append(lm.antonyms()[0].name())
print(set(antonyms))
#it give all  antonyms word related to the ahead which is present in the wordnet
#in the if block there is the only index valued are given means which take the starting elemnet only