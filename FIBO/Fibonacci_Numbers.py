import EasyFiles as ef

# Given: A positive integer n<=25.
# Return: The value of Fn.

# I did a normal recursion and realized my computer couldn't even do 100 calls. The file called 'Playing_with_Fib' has a few cool ways of doing fib sequence if you're trying to run a bigger number than 25... say 5 000 000 or so.


input = ef.getInput() # get the input list
inputValue = int(input[0])

def countFib(index):
	a, b = 0, 1
	for _ in range(index):
		a, b = b, a+b
	return a
ans = countFib(inputValue)
ef.writeOutput( str(ans) ) 

# 0 : 0
# 1 : 1
# 2 : 1
# 3 : 2
# 4 : 3
# 5 : 5

# Value is this value plus last fib sequence
# Except if less than two.. than its the input val