def gcd(x, y):
	if y == 0:
		return x
	return gcd(y , x % y)

def lcm(x, y):
	g = gcd(x, y)
	lcm = (y*x)//g
	return lcm
y = 15
x = 20
print(lcm(x, y))