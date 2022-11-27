import re

phoneNumRegex = re.compile(r'\d{4}-\d{3}-\d{4}')
phoneNumbers = phoneNumRegex.findall('Call me at 0951-698-5620 tomorrow. 0995-265-9628 is my office.')
for i in range(len(phoneNumbers)):
  print('Phone Number Found: ' + phoneNumbers[i])