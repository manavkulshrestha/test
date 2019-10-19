def add(a, b):
	return a+b

def subtract(a, b):
	return a-b

def multiple(a, b):
	return a*b

def factorial(a):
	if a == 0:
		return 1
	return multiply(a, factorial(a-1))

def divide(a, b):
	return a/b