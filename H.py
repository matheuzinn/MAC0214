import math
n,k=list(map(int,input().split()))
if(n/k<2):
	print(10)
else:
	print(5*math.ceil(n/k))
