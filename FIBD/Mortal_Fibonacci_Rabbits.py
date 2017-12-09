import EasyFiles as ef 

input = ef.getInput() # get the input list
duration, lifespan = input[0].split(' ')
duration = int(duration)
lifespan = int(lifespan)
print "d:%d l:%d" % (duration, lifespan)

# Given: Positive integers n<=100 and m<=20
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

#n = months (starts at 1)
#L = lifespan
#born[n] = total[n-1]-born[(n-1)-L] (if n-1==0: 0)(if n-L==0: return 1; if n-L<0: return 0)
#total[n](if n-1==0: 1) = total[n-1]+born[n-1]-born[n-L](if n-L==0: return 1; if n-L<0: return 0) 

totalDic = {}
bornDic = {}

def storeTotal(index, res):
	totalDic[index] = res
	try:
		del totalDic[index-2]
	except:
		pass
def storeBorn(index, res, lifespan):
	bornDic[index] = res
	try:
		del bornDic[(index-2)-lifespan]
	except:
		pass
def total(index, lifespan):
	try:
		return totalDic[index]
	except:
		if index==1:
			res = 1
		else:
			res = total(index-1, lifespan)+born(index-1, lifespan)-born((index-1)-lifespan, lifespan)
			storeTotal(index, res)
		return res
def born(index, lifespan):
	try:
		return bornDic[index]
	except:
		if index<0:
			res = 0
		elif index==0:
			res = 1
		elif index==1:
			res = 0
		else:
			res = total(index-1, lifespan)-born((index-1)-lifespan, lifespan)
			storeBorn(index, res, lifespan)
		return res

ans = total(duration, lifespan)
print "ans: %d" % ans
ef.writeOutput( str( ans ) )



'''
Helpful Examples:
25, 31 => 75025
30, 30 => 832040
35, 29 => 9227437
40, 28 => 102333267
45, 27 => 1134880302
50, 26 => 12585734257
55, 25 => 139572033844
60, 24 => 1547756440188
65, 23 => 17162433794472
70, 22 => 190285454264264
75, 21 => 2109333161649033
'''