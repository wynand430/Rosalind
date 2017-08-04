import EasyFiles as ef 

# Given: Positive integers n<=40 and k<=5.
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
#
# input of 5 3
# 5 = months (n)
# 3 = sexDrive (k)
#
# 1 -> (1)+0kids
# 2 -> (1)+3kids
# 3 -> (4)+3kids
# 4 -> (7)+12kids
# 5 -> (19)pairs at start

input = ef.getInput() # get the input list
months, sexDrive = input[0].split(' ')

months = int(months)
sexDrive = int(sexDrive)

kids = 1 # 1 kids pair to start
aging = 0 # 0 aging at start
adults = 0 # 0 adult pair at start
for month in range(1,int(months)):
	aging = kids
	kids = (sexDrive*adults)	
	adults += aging
	#print "month %d: %d adults, %d kids" % (month, adults,kids)
pairs = adults+kids
ef.writeOutput( str(pairs) ) 