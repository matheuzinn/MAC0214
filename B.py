# 1 <= k <= n
# 1 <= n <= 10^9
# 1 <= x <= max(1,m-k)
# n = max(1,m-k)
 
T = int(input())
for _ in range(T):
	n,k = list(map(int,input().split()))
	kilani=True
	if(n-k<=1):
		if(n%2==0):
			print("Ayoub")
			continue
	print("Kilani")
