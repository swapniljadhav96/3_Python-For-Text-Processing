# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:27:28 2024

@author: suraj
"""

'''----------------7/6/23---8.15------------------------------'''
#pattern matching concept

import re
text1 = " My mobile number is 1345678567"
text2 = " my altenate mobile is 2345532234"
text3="my another international mobile number is (134)-456-8907"
pat1='\d{10}'
pat2='\d\d\d\d\d\d\d\d\d\d'
pat3='\(\d{3}\)-\d{3}-\d{4}'
mob_num=re.findall(pat1,text1)      #Out[21]: ['1345678567']
mob_num
#####
#mob_num=re.findall(text1,pat1)      #Out[13]: []
mob_num=re.findall(pat2,text1)      #Out[25]: ['1345678567']
mob_num
#######
mob_num=re.findall(pat3,text3)      #Out[35]: ['(134)-456-8907']
mob_num

#\d{10}
#\d matches a digit (equivalent to [0-9])
#{10} matches the previous token exactly 10 times
#\(\d{3}\)-\d{3}-\d{4}
#\( matches the character ( with index 4010 (2816 or 508) literally (case sensitive)
#\d matches a digit (equivalent to [0-9])
#{3} matches the previous token exactly 3 times
#\) matches the character ) with index 4110 (2916 or 518) literally (case sensitive)
#- matches the character - with index 4510 (2D16 or 558) literally (case sensitive)
#\d matches a digit (equivalent to [0-9])
#{3} matches the previous token exactly 3 times
#- matches the character - with index 4510 (2D16 or 558) literally (case sensitive)
#\d matches a digit (equivalent to [0-9])
#{4} matches the previous token exactly 4 times
###########################################
#email id matching pattern
import re
text1="my email-id is abcpqr@gmail.com"
text2= "my email id is  abcd.ABCD@gamil.com"
text3=" My offical meil id is abcdgsh123@gmail.com"

pat='[a-zA-Z0-9_.]*@[a-z]*\.com'
mail=re.findall(pat,text1)      #Out[56]: ['abcpqr@gmail.com']
mail

mail=re.findall(pat,text2)      #Out[58]: ['abcd.ABCD@gamil.com']
mail

mail=re.findall(pat,text3)      #Out[60]: ['abcdgsh123@gmail.com']
mail
'''
[a-zA-Z0-9_.]*@[a-z]*\.com:-
Match a single character present in the list below [a-zA-Z0-9_.]
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
A-Z matches a single character in the range between A (index 65) and Z (index 90) (case sensitive)
0-9 matches a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
_. matches a single character in the list _. (case sensitive)
@ matches the character @ with index 6410 (4016 or 1008) literally (case sensitive)
Match a single character present in the list below [a-z]
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
\. matches the character . with index 4610 (2E16 or 568) literally (case sensitive)
com matches the characters com literally (case sensitive)'''

##############################################
text1="my email-id is suraj.chothe@sanjivani.org.in"
pat1='[a-z]*.[a-z]*@[a-z]*\.org.in'
mail=re.findall(pat1,text1)         #Out[64]: ['suraj.chothe@sanjivani.org.in']
mail

'''
[a-z]*.[a-z]*@[a-z]*\.org.in:-
Match a single character present in the list below [a-z]
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
. matches any character (except for line terminators)
Match a single character present in the list below [a-z]
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
@ matches the character @ with index 6410 (4016 or 1008) literally (case sensitive)
Match a single character present in the list below [a-z]
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
\. matches the character . with index 4610 (2E16 or 568) literally (case sensitive)
org matches the characters org literally (case sensitive)
. matches any character (except for line terminators)
in matches the characters in literally (case sensitive)'''

####################################
#
import re
chat1="hi my order #496729 is not received yet"
chat2=" hi I having problem with ordernumber 496729 which is not received"
chat3="hi my order 496729 is having an issue"

pat='order[a-z #]*[0-9]*'       #another patt 'order[^\d]*\d*'
mat=re.findall(pat,chat1)        
mat

'''
order[a-z #]*[0-9]*:-
order matches the characters order literally (case sensitive)
Match a single character present in the list below [a-z #]
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
 # matches a single character in the list  # (case sensitive)
Match a single character present in the list below [0-9]
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
0-9 matches a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
'''

######################
#anotehre pattern for above code
import re
chat1="hi my order #496729 is not received yet"
chat2=" hi I having problem with ordernumber 496729 which is not received"
chat3="hi my order 496729 is having an issue"
pat='order[^\d]*\d*'
mat=re.findall(pat,chat1)        
mat
'''
order[^\d]*\d*:-
order matches the characters order literally (case sensitive)
Match a single character not present in the list below [^\d]
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
\d matches a digit (equivalent to [0-9])
\d matches a digit (equivalent to [0-9])
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)'''
#############
#in the above  example we only want the number so use trhe followig pattern
import re
chat1="hi my order #496729 is not received yet"
chat2=" hi I having problem with ordernumber 496729 which is not received"
chat3="hi my order 496729 is having an issue"
pat='order[^\d]*(\d*)'
mat=re.findall(pat,chat2)        
mat


######################
import re
chat3="hi my order #496729 is not received yet"
pat='order[^\d]*(\d*)'
mat=re.findall(pat,chat3)        
mat

################
import re
chat3="hi my order 496729 is having an issue with the 3000$ market"
pat='order[^\d]*(\d*)'
mat=re.findall(pat,chat3)        
mat
#####################
#we can write the sepaert  the function for and then call thet function as like noraml with the function name

def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches
    
get_pattern_match('order[^\d]*(\d*)',chat1) 
###############################
#retrieve email id and phone
chat1='hi: you ask lot of question 123456787654,abc@xyz.com'
chat2='hi:'






#########################
#
text='''Born	Elon Reeve Musk
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
    Spouses	
    Justine Wilson
​
    ​(m. 2000; div. 2008)​
    Talulah Riley
​
    ​(m. 2010; div. 2012)​
​
    ​(m. 2013; div. 2016)​
    Partner	Grimes (2018–2021)[1]
    Children	10[a][3]
    Parents	
    Errol Musk (father)
    Maye Musk (mother)
    Family	Musk family
    Signature'''
get_pattern_match(r'age (\d+)', text)   #Out[20]: ['51']
match=get_pattern_match(r'Born(.*)',text)   #Out[22]: 'Elon Reeve Musk'
match[0].strip()
##############
