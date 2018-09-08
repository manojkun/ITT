#!/usr/bin/python3
print("Please Enter Matrix Order")
m=int(input())
n=int(input())
print("enter Matrix")
a = [ [0]*n for i in range(m) ]
b = [ [0]*m for i in range(n) ]
for i in range(m):
        a[i] = input().split(' ')
for i in range(m):
    for j in range(n):
        b[j][i] = a[i][j]
print("The transpose is")
for i in range(n):
    for j in range(m):
            print(b[i][j],end='')
            print(" ",end='')
    print("")

