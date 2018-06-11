#!/usr/bin/python3


import os

import numpy

x= """
Press 1 : To continue
   """

print ( x )

ch = input("enter your choice :")
if int(ch)==1:
	print ("MatrixA")
	rowsA=int(input("No. of rows:"))
	colsA=int(input("No.of columns:"))
	A=numpy.random.random((rowsA,colsA))
	print (A)
	print ("MatrixB")
	rowsB=int(input("No. of rows:"))
	colsB=int(input("No.of columns:"))
	B=numpy.random.random((rowsB,colsB))
	print (B)
	C=A+B
	
	print("matrix C")
	print (C)
	
	file=input("enter the filename")
	fp=open(file,"w")
	fp.write(str(C))
	

	


	
	
	






































