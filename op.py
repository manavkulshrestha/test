def add(a, b):
	return a+b

def subtract(a, b):
	return a-b

def multiple(a, b):
	return a*b

def factorial(a):
	ret = a
	for i in range(1, a):
		ret *= i
	return ret