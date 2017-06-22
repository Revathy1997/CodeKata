a=int(input("enter the number"))
z=1
if a==0:
	print("the factorial zero is 1")
else:
	for i in range(1,a+1):
		z=z*i
	print("the factorial of",a,"is",z)		
