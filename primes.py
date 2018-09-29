#!/usr/bin/python

lim=int(input())
i=2
flg=0
for i in range(2,lim):
    flg=0
    for j in range(2,i):
        if i%j==0:
            flg=1
            break
    if flg==0:
        print(i)
