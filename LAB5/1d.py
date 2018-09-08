#!/usr/bin/python3
print("Please Enter Matrix Order")
n=int(input())
print("enter Matrices")
a = [ [0]*n for i in range(n) ]
b = [ [0]*n for i in range(n) ]
c = [ [0]*n for i in range(n) ]
for i in range(n):
        a[i] = input().split(' ')
for i in range(n):
        b[i] = input().split(' ')
for i in range(n):
    for j in range(n):
        c[i][j] = int(a[i][j]) + int(b[i][j])
            
print("The Sum is")
for i in range(n):
    for j in range(n):
            print(c[i][j],end='')
            print(" ",end='')
    print("")

