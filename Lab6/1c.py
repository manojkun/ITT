#!/usr/bin/python
words=input("Enter words: ").split(' ')
words.sort()
for word in words:
    print(word+" ",end='')
