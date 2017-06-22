a=int(input("enter the number"))
b=a
sum=0
len1=len(str(a))
print("given number length is",str(len1))
while(b!=0):	
	q=b%10
	r=b//10
	b=r
	sum=sum+q**len1
if sum==int(a):
	print("armstrong")
else:
	print("not armstrong")
