import EasyFiles as ef 
import time

# Given: A positive integer n<=25.
# Return: The value of Fn.

# I did a normal recursion and realized my computer couldn't even do 100 calls. Then I made my fib() version which is set up to handle a max of ~ 1000

# Then I realized I wanted to know bigger numbers so
# I made largeFib()... I tried running 1 million but then I realized my memory was exploding, because I wasn't removing previous dicitonary values.
# set it up to only store 2 dictionary value at a time...
# ran one million in about 13 seconds with a pretty small amount of memory usage. This was with an iteration of 400.
# changing the iteration to 200 or 100 didn't affect the time (within error
# Data in seconds (minutes & seconds to nearest sec)
# .5 million => 3.9
# 1 milion => 13.1
# 2 million => 47.5
# 3 million => 104.6 (1min,45sec)
# 4 million => 179.7 (4min)
# 5 million => 279.2 (4min,39sec)
# How can I bring this down...
# I'm gonna try a super basic counting method
# this will use two vars a & b..
# they'll just count up
# that saves me a million dictionary searches
# plus some deletes
# Data in seconds (minutes & seconds to nearest sec)
# .5 million => 2.7
# 1 milion => 10.3
# 2 million => 40.9
# 3 million => 94.0 (1min,34sec)


input = ef.getInput() # get the input list

fibDic = {} # stores previous fib sequences
iterate = {} # stores how many times each fib value is accessed... this was mostly for testing

def store(index, res):
	#  "fibDic[%d] = %d" % (index, res)
	fibDic[index] = res
	try:
		del fibDic[index-2]
	except:
		pass
	try:
		iterate[index]+=1
	except:
		iterate[index]=1

def largeFib(index):
	iteration = 200
	temp = iteration
	while temp+iteration < index:
		fib(temp)
		temp+=iteration
	return fib(index)
	
def fib(index):
	# print "fib(%d)" % (index)
	try:
		return fibDic[index]
	except:
		if index < 2:
			res = index
		else:
			res = fib(index-1)+fib(index-2)
		store(index, res)
		return res

def countFib(index):
	a, b = 0, 1
	for _ in range(index):
		a, b = b, a+b
	return a
	
inputValue = int(raw_input('Index of fib number? '))
# start = time.time()
# largeFib(inputValue)
# print "largeFib(%d): %s" % (inputValue,time.time()-start)
start = time.time()
countFib(inputValue)
print "countFib(%d): %s" % (inputValue,time.time()-start)
# ef.writeOutput( ans ) 

# 0 : 0
# 1 : 1
# 2 : 1
# 3 : 2
# 4 : 3
# 5 : 5

# Value is this value plus last fib sequence
# Except if less than two.. than its the input val