#! /usr/bin/env python3.3

#	Russell Folk
#	November 29, 2012
#	Project Euler #1
#	Find the sum of all the multiples of 3 or 5 below 1000.

#	end is 990 because the cycle will not complete before 1000.
end		= 990

total	= 0
num		= 0

#	Could be done with mod 3 and 5 but will be less efficient
while num < end :
	num += 3
	total	+= num
	num += 2
	total	+= num
	num += 1
	total	+= num
	num	+= 3
	total	+= num
	num	+= 1
	total	+= num
	num	+= 2
	total	+= num
	num	+= 3
	total	+= num

num	+= 3
total	+= num
num	+= 2
total	+= num
num	+= 1
total	+= num
num	+= 3
total	+= num

print ( "The total of all the multiples of 3 and 5 added together is: "
	+ str ( total ) )
