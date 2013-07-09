#! /usr/bin/env python3.3

#	Russell Folk
#	December 5, 2012
#	Project Euler #15
#	How many routes are there through a 20×20 grid?

def combination ( n, k ) :
	return factorial ( n ) / ( factorial ( k ) * factorial ( n - k ) )

def factorial ( n ) :
	if n < 2 :
		return 1
	return n * factorial ( n - 1 )

xGrid	= 20
yGrid	= 20

paths	= combination ( xGrid + yGrid , xGrid )

print ( "The number of unique paths is " + str ( paths ) )