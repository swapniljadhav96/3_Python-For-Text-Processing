# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:17:18 2023

@author: Dell
"""

import re
text1="My mobile number is 9850603297"
text2="my alternate mobile is 8530234567"
text3="My international mobile number is(124)-456-75432"
pat1='\d{10}'
mob_num=re.findall(pat1,text1)
mob_num
pat2='\(\d{3}\)-\d{3}-\d{5}'
mob_num=re.findall(pat2,text3)
mob_num
####################################


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
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat2)
matches
######################################
import re

chat1=' Hello, I am having an issue with my order # 412889912'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat1)
matches
######################################
chat3=' My order 412889912 is having an issue, I was charged 300$ when online it says 280$'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat3)
matches
##################################
def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches

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

get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})|[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat2)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat3)


###########################################
text='''
Born	Elon Reeve Musk

June 28, 1971 (age 51)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	

    Founder, CEO and chief engineer of SpaceX
    CEO and product architect of Tesla, Inc.
    Owner, CTO and chairman of Twitter
    President of the Musk Foundation
    Founder of the Boring Company, X Corp. and X.AI
    Co-founder of Neuralink, OpenAI, Zip2 and X.com (part of PayPal)

'''
get_pattern_match(r'age (\d+)', text)
match=get_pattern_match(r'Born(.*)',text)
match[0].strip()

match1=get_pattern_match(r'Born.*\n(.*)\(age', text)
match1
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
#1. Extract all twitter handles from following text. Twitter handle is the text that appears after https://twitter.com/ and is a single word. Also it contains only alpha numeric characters i.e. A-Z a-z , o to 9 and underscore _
text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern = 'https://twitter\.com/([a-zA-Z0-9_]+)'

re.findall(pattern, text)
######################################################
#2. Extract Concentration Risk Types. It will be a text that appears after "Concentration Risk:", In below example, your regex should extract these two strings
text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
pattern = 'Concentration of Risk: ([^\n]*)'

re.findall(pattern, text)
####################################################
#Companies in europe reports their financial numbers of semi annual basis
# and you can have a document like this. To exatract quarterly and semin annual 
#period you can use a regex as shown below
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

pattern = 'FY(\d{4} (?:Q[1-4]|S[1-2]))'
matches = re.findall(pattern, text)
matches
#######################################
