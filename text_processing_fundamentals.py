# -*- coding: utf-8 -*-
"""


@author: Dell
"""

import re
'''
google tesla company filings
click to Annual & Quarterly Reports 
apply filters
click on 10Q pdf
goto-Notes to Consolidated Financial Statements
(unaudited)
Now we want to extract title
 'Summary of Significant Accounting Policies'
 goto regex101.com
'''
#let us assume we have simple text as below,we want to extract phone number
'''
goto regex101.com,on right bootom there are various patterns 
and their meaning,suppose I want to extract any digit,there is pattern
\d
copy the text1 in text string window
and write \d\d\d\d\d\d\d\d\d\d in regular expression window
observe the match information window
The 10 digit number is matched
But writing \d\d\d\d\d\d\d\d\d\d is cumbersome
In right bottom window there is pattern for multiple digits
exactly 3 of a :a{3}
here a is \d :
goto regular expression window
type-\d{10}
and you will get 9991116666
------------------------
But what about (999)-333-7777
Now let us try to match this,first we will try Elon,go to
 regular expression window,write Elon
 you will find Elon match in text
 Now we want ()
Assume '(' is a special charecter
\( ,now open ( is matching
-We have exactly three digits
\d{3},go to regular expression window and type \(\d{3}
Now we got (999
If we try \(\d{3}\) now we are getting (999)
If we will try \(\d{3}\)-\d{3}-\d{4} and we are getting (999)-333-7777
If we will try \d{10} or \(\d{3}\)-\d{3}-\d{4}
-There is pattern for OR expression,right bottom window
a|b
The pattern will be  \(\d{3}\)-\d{3}-\d{4}|\d{10}
Goto regular expression window and type  \(\d{3}\)-\d{3}-\d{4}| \d{10}
and we are getting
9991116666
(999)-333-7777

Matches either what is before the | or what is after it - in this case `a` or `b`.


'''
import re

text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern=r'\d\d\d\d\d\d\d\d\d\d'
matches=re.findall(pattern,text)
matches


text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern=r'\d{10}'
matches=re.findall(pattern,text)
matches



pattern = '\(\d{3}\)-\d{3}-\d{4}'
matches=re.findall(pattern,text)
matches



import re
text1='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'

matches = re.findall(pattern, text1)
matches
#######################################
'''
let us try 
following pattern
A protracted; legal battle; over a 32-carat;
 Golconda diamond-  
 We want any charecter except ; and -
 pattern will be [^;-]
 Goto regular expression window and type [^;-]
 and you will get the text
 '''
text2='A protracted; legal battle; over a 32-carat;Golconda diamond-'
pattern='[^;-]'
matches=re.findall(pattern,text2)
matches  
###############################
'''

Now let us try our report,we want to extract-
Note 1 – Summary of Significant Accounting Policies
pattern= Note \d - [^\n]
It will match 
Note 1 – S
'copy the report in test string window'
-type in RE window-Note \d - [^\n]*
text matched will be-Note 1 - Summary of Significant Accounting Policies
'''
text3='''
Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.'''
pattern='Note \d - [^\n]'
matches=re.findall(pattern,text3)
matches
'''
Now  we want more charecters from it,go to right bottom 
window there is
one or more of a--- a+
'''
pattern='Note \d - [^\n]+'
matches=re.findall(pattern,text3)
matches
'''
Now we are getting 
['Note 1 - Summary of Significant Accounting Policies']
'''
#Now let us try
pattern='Note \d - [^\n]*'
matches=re.findall(pattern,text3)
matches
#['Note 1 - Summary of Significant Accounting Policies']
# but we want only'[Summary of Significant Accounting Policies]'
#go to right bottom
#there is option capture everything enclosed for that
#we need to enclose it ()
pattern='Note \d - ([^\n]*)'
matches=re.findall(pattern,text3)
matches
###########################################3
'''
Now let us take another text
Extract financial periods from a company's financial reporting
'''
text4 = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
#Quarters can be Q1,Q2,Q3 or Q4 not Q5 or Q6
#let us copy this text in Test string window

pattern='FY\d{4} Q\d'
matched=re.findall(pattern,text4)
matched
#Now go to right bottom window and there is 
#option single charcter a,b or c[abc]
#now try second pattern 'FY\d{4} Q[1234]'
pattern='FY\d{4} Q[1234]'
matched=re.findall(pattern,text4)
matched
#you can even give range
pattern='FY\d{4} Q[1-4]'
matched=re.findall(pattern,text4)
matched
#################################
#what if your text comprises of
text5 = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''
pattern='FY\d{4} Q[1-4]'
matched=re.findall(pattern,text5)
matched
#####################################
#Now we are getting ['FY2021 Q1']
#In order to solve this issue,re.IGNORECASE
pattern1='FY\d{4} Q[1-4] |fy\d{4} Q[1-4]'

matched=re.findall(pattern1,text5)
matched

#####################################
matched=re.findall(pattern,text5,re.IGNORECASE)
matched
#['FY2021 Q1', 'fy2020 Q4']
#######################################
#Now let us assume we want only 2021 Q1 and 2020 Q4,then 
#you can get extract through(...)
pattern='FY(\d{4} Q[1-4])'
matched=re.findall(pattern,text5,re.IGNORECASE)
matched
##########################
#Now let us assume that we want to find financial number

text6 = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''
# we want $4.85 and $3
#simply $ can not be used as it is special symbol
#pl ref right bottom window
#Even . charecter can not be used.
# it is also special symbol
pattern = '\$[0-9\.]+'
matched = re.findall(pattern, text6)
matched
#If we do not want $
pattern = '\$([0-9\.]+)'
matched = re.findall(pattern, text6)
matched
