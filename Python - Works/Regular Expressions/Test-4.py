# WAP to Verify the Given Mail Address
# E-mail Address should include : * 1-20 uppercase or lowercase letters, numbers and .%+-
#                                 * @ Symbol
#                                 * 2-20 uppercase or lowercase letters, numbers and .-
#                                 * . Symbol
#                                 * 2-3 Uppercase or lowercase letters

import re

Mail = 'Prabhakar108@gmail.com, Prabhakar_gmail.com, Prabhakar@yahoo.co, Prabhakar_567@Yahoo.com, Prabhakartinder.com, Prabhakar_108@linkedin.com, Prabhakar_108linkedin.com'

regex = re.findall(r'[\w.%+-]{1,20}@[\w.-]{2,20}.\w{2,3}', Mail)                  #\w contains(A-Z a-z 0-9 _ )
print (regex)
print (len(regex))