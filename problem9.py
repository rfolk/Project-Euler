#! /usr/bin/env python3.3

#	Russell Folk
#	December 2, 2012
#	Project Euler #9
#	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#	Find the product abc.

goal		= 1000
product	= 0

#	as max is 1000, c must be 500 or less.
cMax	= 500
cMin	= 400
#	b must be less than c, so we will use 400.
bMax	= 400
bMin	= 300
#	a must be less than b, so we will use 300.
aMax	= 300
aMin	= 200

for c in range ( cMin , cMax ) :
	for b in range ( bMin , bMax ) :
		for a in range ( aMin , aMax ) :
			if ( a + b + c == goal ) and ( (a ** 2) + (b ** 2) == (c ** 2) ) :
				product	= a * b * c

print ( "The product of the Pythagorean triplet is " + str ( product ) )
