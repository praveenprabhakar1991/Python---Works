# WAP to Verify the Given Phone Numbers
# All Numbers should have : * 3 Starting Digits and '-' sign
#                           * 3 middle Digits and '-' sign
#                           * 4 Digits in the end

import re

Numbers = '987-456-0123, 987-456-123, 456-879-2031, 789_564-1230, 789-654-1302, 777-658_9412, 849-465-0321'

regex = re.finditer(r'\d{3}-\d{3}-\d{4}', Numbers)                  # \d contains (0-9) digits
for reg in regex:
    print(reg)

regex = re.findall(r'\d{3}-\d{3}-\d{4}', Numbers)
print(regex)
print(len(regex))
