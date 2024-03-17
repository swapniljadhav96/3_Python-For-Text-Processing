# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:17:18 2023

@author: Dell
"""

from PyPDF2 import PdfFileReader
# importing required modules
from PyPDF2 import PdfReader

# creating a pdf reader object
reader = PdfReader('c:/10-python/python_tutorial.pdf')

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
page = reader.pages[10]

# extracting text from page
text = page.extract_text()
print(text)
###########################################
import re
chat2='Hi: I have a problem with my order number 412889912'
pattern='order [^\d]*(\d)'
matches = re.findall(pattern, chat2)
matches


import re
chat2='Hi: I have a problem with my order number 412889912'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat2)
matches
######################################
import re

chat1='Hi: Hello, I am having an issue with my order # 412889912'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat1)
matches
######################################
chat3='NLPbasics: My order 412889912 is having an issue, I was charged 300$ when online it says 280$'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat3)
matches
##################################
def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]

get_pattern_match('order[^\d]*(\d*)', chat1)
################################
#Retrieve email id and phone
chat1 = 'Hi: you ask lot of questions   1235678912, abc@xyz.com'
chat2 = 'Hi: here it is: (123)-567-8912, abc@xyz.com'
chat3 = 'Hi: yes, phone: 1235678912 email: abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)

get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)

get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)
##########################################
#-----Phone number-----
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat2)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat3)
###########################################
#text is taken from wikipedia
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 50)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa (1971–present)
Canada (1971–present)
United States (2002–present)
Education	University of Pennsylvania (BS, BA)
Title	
Founder, CEO and Chief Engineer of SpaceX
CEO and product architect of Tesla, Inc.
Founder of The Boring Company and X.com (now part of PayPal)
Co-founder of Neuralink, OpenAI, and Zip2
Spouse(s)	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''
get_pattern_match(r'age (\d+)', text)
get_pattern_match(r'Born(.*)\n', text).strip()
get_pattern_match(r'Born.*\n(.*)\(age', text).strip()
get_pattern_match(r'\(age.*\n(.*)', text)

#######################################
def extract_personal_information(text):
    age = get_pattern_match('age (\d+)', text)
    full_name = get_pattern_match('Born(.*)\n', text)
    birth_date = get_pattern_match('Born.*\n(.*)\(age', text)
    birth_place = get_pattern_match('\(age.*\n(.*)', text)
    return {
        'age': int(age),
        'name': full_name.strip(),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()
    }
extract_personal_information(text)
#################################################
text = '''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 64)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Stanford University (drop-out)
Occupation	Chairman and MD, Reliance Industries
Spouse(s)	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent(s)	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''
extract_personal_information(text)
#########################################
