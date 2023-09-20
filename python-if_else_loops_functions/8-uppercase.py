#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
       char_to_change = ord(str[i])
       if char_to_change >= 97 and char_to_change <= 122:
           char_to_change -= (ord('a') - ord('A'))
           print("{}".format(chr(char_to_change)), \
end='' if i < len(str) -1  else "\n")
       else:
           print("{}".format(chr(char_to_change)), \
end='' if i < len(str) -1  else "\n")
