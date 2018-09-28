#!/usr/bin/python
import string
st = list(input())
for c in string.punctuation:
    while c in st:
        st.remove(c)
print("".join(st))
