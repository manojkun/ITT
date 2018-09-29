#!/usr/bin/python
l=input("Enter list elements: ").split(' ')
if l==list(reversed(l)):
    print("Palindrome")
else:
    print("Not Palindrome")
