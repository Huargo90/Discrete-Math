def modp (n,m,k):
	ans = 1
	for i in range(m):
		ans = (ans*n)%k
	return ans

def letter (n):
	print chr(n+96)

