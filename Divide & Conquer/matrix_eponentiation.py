def multiply(x,y):
	if len(y)==2:
		a = x[0]*y[0] + x[1]*y[1]
		b = x[1]*y[0] + x[3]*y[1]
		return [a,b]
	a = x[0]*y[0] + x[1]*y[2]
	b = x[0]*y[1] + x[1]*y[3]
	c = x[2]*y[0] + x[3]*y[2]
	d = x[2]*y[1] + x[3]*y[3]
	return [a,b,c,d]
def matrix_expo(x,N):
	if N==1:
		return x
	if N%2==0:
		ans = matrix_expo(x,N//2)
		return multiply(ans,ans)
	return multiply(x,matrix_expo(x,N-1))
A = [1,1,1,0]
v = [1,1]


