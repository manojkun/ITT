#!/usr/bin/python3

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

n=int(input("enter n: "))
for i in range(n):
    print(fib(i))

