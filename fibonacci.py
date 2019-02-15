N=int(input())
aa=1
bb=1
print(aa,bb,end=" ")
for i in range(3,N+1):
	c=aa+bb
	print(c,end=" ")
	aa=bb
	bb=c
