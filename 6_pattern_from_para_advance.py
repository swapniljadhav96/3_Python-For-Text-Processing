# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:28:50 2024

@author: suraj
"""

"""-----------------8\6\23---8.30--------------------------------"""
#find the date of birth
match1=get_pattern_match(r'Born.*\n(.*)\(age',text)    #Out[23]: ['June 28, 1971 ']
match1
"""/
Born.*\n(.*)\(age:-
Born matches the characters Born literally (case sensitive)
. matches any character (except for line terminators)
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
\n matches a line-feed (newline) character (ASCII 10)
1st Capturing Group (.*)
. matches any character (except for line terminators)
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
\( matches the character ( with index 4010 (2816 or 508) literally (case sensitive)
age matches the characters age literally (case sensitive)"""

############
#find the palce of the birth
get_pattern_match(r'\(age.*\n(.*)',text)    #Out[25]: ['Pretoria, Transvaal, South Africa']

'''
\(age.*\n(.*);-
\( matches the character ( with index 4010 (2816 or 508) literally (case sensitive)
age matches the characters age literally (case sensitive)
. matches any character (except for line terminators)
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
\n matches a line-feed (newline) character (ASCII 10)
1st Capturing Group (.*)
. matches any character (except for line terminators)
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)'''
################################################

#we can write the above code in the single function
def extract_personal_info(text):
    age=get_pattern_match('age (\d+)', text)
    full_name=get_pattern_match('Born(.*)\n', text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age', text)
    birth_place=get_pattern_match(r'\(age.*\n(.*)',text)
    return{
        'age':age,
        'name':full_name,
        'birth_date':birth_date,
        'birth_place':birth_place
     }
extract_personal_info(text)

################################################
#same text for the mukesh ambani
text='''Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent	
Dhirubhai Ambani (father)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)'''


def get_pattern(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches
    
get_pattern('order[^\d]*(\d*)',chat1) 

get_pattern(r'age (\d+)', text)  
############
match=get_pattern(r'Born(.*)',text)  
match[0].strip()
###########
match1=get_pattern(r'Born.*\n(.*)\(age',text)  
match1
################
get_pattern(r'\(age.*\n(.*)',text)

###########################
#we can write the the above code in the function form
def extract_personal_info(text):
    age=get_pattern('age (\d+)', text)
    full_name=get_pattern('Born(.*)\n', text)
    birth_date=get_pattern('Born.*\n(.*)\(age', text)
    birth_place=get_pattern(r'\(age.*\n(.*)',text)
    return{
        'age':age,
        'name':full_name,
        'birth_date':birth_date,
        'birth_place':birth_place
     }
extract_personal_info(text)

#####################################
#1. Extract all twitter handles from following text. Twitter handle is the text =
text='''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, 
on Tesla's products can be found at https://www.tesla.com/. Also here are 1 
for tesla related news,
https://twitter.com/dummy_2_tesla
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
'''

pattern='https://twitter\.com/([a-zA-Z0-9_]+)'
re.findall(pattern,text)

######################################
#2.Extractthe concentration risk type .It will be a text that appera after 
text='''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31,
'''

pattern='Concentration of Risk: ([^\n]*)'

re.findall(pattern,text)            #Out[55]: ['Credit Risk']
#################################################
#companies 
#to uderstant the patttern use the 'regex101.com/
text='''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billi BMW's gross cost 
of operating vehicles in FY2021 S1 was $8 billion'''


pattern='FY(\d{4} (?:Q[1-4]|S[1-2]))'       #match this ?:
matches=re.findall(pattern,text)
matches


"""FY(\d{4} (?:Q[1-4]|S[1-2])):-
FY matches the characters FY literally (case sensitive)
1st Capturing Group (\d{4} (?:Q[1-4]|S[1-2]))
\d matches a digit (equivalent to [0-9])
{4} matches the previous token exactly 4 times
  matches the character   with index 3210 (2016 or 408) literally (case sensitive)
Non-capturing group (?:Q[1-4]|S[1-2])
1st Alternative Q[1-4]
Q matches the character Q with index 8110 (5116 or 1218) literally (case sensitive)
Match a single character present in the list below [1-4]
1-4 matches a single character in the range between 1 (index 49) and 4 (index 52) (case sensitive)
2nd Alternative S[1-2]
S matches the character S with index 8310 (5316 or 1238) literally (case sensitive)
Match a single character present in the list below [1-2]
1-2 matches a single character in the range between 1 (index 49) and 2 (index 50) (case sensitive)"""

####################################################
#extract the phone number
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777'''

pattern='\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches=re.findall(pattern,text)
matches
###################################################
#we want text imegtaly affter the 'note' on th e same line
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell 
solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''

pattern='Note \d - ([^\n]*)'
matches =re.findall(pattern,text)
matches                             #Out[69]: ['Overview', 'Summary of Significant Accounting Policies']

#############################################
#extract the finacila periods fron a company finacial reporting
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''

pattern='FY\d{4} Q[1-4]'
matches=re.findall(pattern,text)
matches                     #Out[73]: ['FY2021 Q1', 'FY2020 Q4']

##################################################
#case sensetive pattern match using the flages
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''

pattern='FY\d{4} Q[1-4]'
matches=re.findall(pattern,text,flags=re.IGNORECASE)
matches
                #Out[77]: ['FY2021 Q1', 'fy2020 Q4']

#####################################################
#extrcat only finalcial number

text ='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''

pattern='\$([0-9\.]+)'
matches=re.findall(pattern,text)
matches                     #Out[82]: ['4.85', '3']

'''\$([0-9\.]+)
\$ matches the character $ with index 3610 (2416 or 448) literally (case sensitive)
1st Capturing Group ([0-9\.]+)
Match a single character present in the list below [0-9\.]
+ matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedy)
0-9 matches a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
\. matches the character . with index 4610 (2E16 or 568) literally (case sensitive) 
'''

##############################
TExt data processing for data processing are the conccluded
