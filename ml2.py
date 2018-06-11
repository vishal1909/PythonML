#!/usr/bin/python3


import os

import numpy 

x= """
Press 1 : To continue
   """

print ( x )
"""
ch = input("enter your choice :")
if int(ch)==1:
	print ("MatrixA")
	rowsA=int(input("No. of rows:"))
	colsA=int(input("No.of columns:"))
	numpy.array((rowsA,colsA))
	for i in range(0,rowsA):
		for j in range(0,colsA):
			A=numpy.array((rowsA,colsA))
			A[i][j]=int(input())
"""


A=numpy.mat("0,1,2,3;2,3,4,5;1,1,5,8")
print (A)

B=numpy.mat("2,3,5,7;6,9,0,4;1,5,43,2")
print (B)
C=A+B
print("Matrix C after addition",C)
shape=C.shape
print ("Shape of matrix C", shape)
combination=C.reshape(2,3)
print ("Shape of matrix C", combination)




