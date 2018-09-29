#!/usr/bin/python
import string
st = list(input("Enter String: "))
for c in string.punctuation:
    while c in st:
        st.remove(c)
print("".join(st))
