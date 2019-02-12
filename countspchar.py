cc=input()
a=b=c=0
for i in range(0,len(cc)):
	if cc[i].isalpha():
		a+=1
	elif cc[i].isnumeric():
		b+=1
	else:
		c=c+1
print(c)
