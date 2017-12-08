import EasyFiles as ef 

input = ef.getInput() # get the input list
munth, lifespan = input[0].split(' ')
munth = int(munth)
lifespan = int(lifespan)

# Given: Positive integers n<=100 and m<=20
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
#
# input of 3 3
# 5 = months (n)
# 3 = liveSpan (k)

### 3
# 0 = 1
# 1 = 0
# 2 = [1]+[0]
# 3 = [2]+[1]
# 4 = [3]+[2]-[0]
# 5 = [4]+[3]-[1]
# 6 = [5]+[4]-[3]
# 7 = [6]+[5]-[4]
# 8 = [7]+[6]-[5]

### 10
# 0 = 1
# 1 = 0
# 2 = [1]+[0]
# 3 = [2]+[1]
# 4 = [3]+[2]
# 5 = [4]+[3]
# 6 = [5]+[4]
# 7 = [6]+[5]
# 8 = [7]+[6]
# 9 = [8]+[7]
# 10 = [9]+[8]
# 11 = [10]+[9]-[0]
# 12 = [11]+[9]-[1]

seq =[1,0]

def bunny_machine(months, lifespan):
	global seq
	if months < len(seq):
		return seq[months]
	else:
		if months > (lifespan):
			death_shift = bunny_machine(months-1-lifespan,lifespan)
		else:
			death_shift = 0
		mod1 = bunny_machine(months-1,lifespan)
		mod2 = bunny_machine(months-2,lifespan)
		answer = mod1+mod2-death_shift
		print "months (%d): [%d]+[%d] -[%d]= %d" % (months, mod1, mod2, death_shift, answer)
		seq.append(answer)
		return answer


bunny_machine(munth,lifespan)
print seq[munth]









ef.writeOutput( str( seq[munth] ) )

# fib()