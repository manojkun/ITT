#!/usr/bin/python
str=input()
str2 = ""
for i in str:
    str2 += chr(97+(ord(i)-97+13)%26)
print(str2)
