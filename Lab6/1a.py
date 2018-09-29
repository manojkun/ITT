#!/usr/bin/python
str=input("Enter String: ")
a = list(str)
if a == list(reversed(a)):
    print("Palindrome")
else:
    print("not Palindrome")
