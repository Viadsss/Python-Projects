def isPhoneNumber(text):
  if len(text) != 13:
    return False
  for i in range(0,4):
    if not text[i].isdecimal():
      return False
  if text[4] != '-':
    return False
  for i in range(5,8):
    if not text[i].isdecimal():
      return False
  if text[8] != '-':
    return False
  for i in range(9,13):
    if not text[i].isdecimal():
      return False
  return True

message = 'Call me at 0951-698-5620 tomorrow. 0995-265-9628 is my office.'
for i in range(len(message)):
  chunk = message[i:i+13]
  if isPhoneNumber(chunk):
    print("Phone number found: " + chunk)
print('Done')