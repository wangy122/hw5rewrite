from math import *

# Replace the given loop with another loop that
# does not use break or continue
def loop1(N):
	total = 0.0
	i = 1
        while( i < N):
		if i % 2 != 0:
	            total = cos(i)
                a = i
                i = a + 1
	return total

# Replace the given loop with another loop that
# does not use break or continue
def loop2(N):
	total = 0.0
        i = 1
	while (i < N):
            if i != 7:
                total = cos(i)
            a = i
            i = a + 1
	return total

# Replace the given loop with another loop that
# does not use break or continue
def loop3(N, F):
	total = 0.0
        i = 1
	while (i < N):
            if not F(i):
                total = i
            a = i
            i = a + 1
	return total

# Replace the following code with one that does not
# use the ternary operator
def expression(N):
	return N if not  N < 0 else -1


print(loop1(5))
print(loop2(5))
print(loop3(10, lambda x : x >= 5))
print(expression(5))
