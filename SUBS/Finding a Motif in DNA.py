import EasyFiles as ef 

# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

input = ef.getInput() # get the input list

s = input[0]
t = input[1]


tracking = {} # sStartIndex:totalCharMatched
found = '' # sStartIndex

# Idea is to go one char at a time in string s
# If the current char in string is matches first character of t
# a new entry is created in the tracking dictionary
# this entry is the current index of s we're on 
# (since we print this out at the end)
# and the index of which char of t we've verified
# so {"start index in s of what we're tracking ":"index of char in t verified so far}
# Then I move on to the next character
# I first check each key in the dictionary to see
# if the current char in s matches the next index of t
# if there is no next index of t -- we remove the entry
# from the tracking and move the start index +1 to found array
#
# this ends up never going backwards on an array which is nice
# this is built for large multi million length s and t strings

def setTracking(sStartIndex,totalCharMatched): # how we set an item in the tracking dict
	# print "setTracking: %r,%r" % (sStartIndex,totalCharMatched)
	tracking[sStartIndex] = totalCharMatched
	if totalCharMatched+1 == len(t):
		markFound(sStartIndex)

def markFound(sStartIndex): # mark an entry as found and remove from tracking
	# print "markFound: %r" % (trueValue)
	global found
	trueValue = sStartIndex+1
	found+="%d " % (trueValue)
	stopTracking(sStartIndex)
	
def stopTracking(sStartIndex):
	del tracking[sStartIndex]

def checkTracking(char):
	keys = [] # Have to store values of keys
	for key in tracking: # since I can't modify dict length
		keys.append(key) # While in the middle of for loop
	for key in keys: # for each value in tracking
		if char == t[tracking[key]+1]: # if char == this value:
			setTracking(key,(tracking[key]+1))
			# setTracking(currentSStartIndex,totalCharMatched):
		else: # else:
			stopTracking(key) # stopTracking(tIndex)

# main()
for i,char in enumerate(s):
	checkTracking(char) # check current tracking
	firstTCharIndex = 0; # start more tracking?
	firstTChar = t[firstTCharIndex]
	# if current s char is same as first t char
	# we'll start tracking from this spotClear
	# to see if the following values are going to match
	if char==firstTChar:
		setTracking(i,firstTCharIndex)
	
ef.writeOutput( found )