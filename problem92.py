#! /usr/bin/env python3.3

# Russell Folk
# July 9, 2013
# Project Euler #92

# A number chain is created by continuously adding the square of the digits in
# a number to form a new number until it has been seen before.
#
# For example,
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless
# loop. What is most amazing is that EVERY starting number will eventually
# arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?

import time

squares = []
numbers = []

start = time.perf_counter()

for i in range ( 10 ) :
  squares.append ( i * i )

for i in range ( 568 ) :
  numbers.append ( 0 )
numbers [ 1 ]  = -1
numbers [ 89 ] =  1

def squareOfDigits ( n ) :
  sumOfSquares  = 0
  while n >= 1 :
    sumOfSquares  += squares[ n % 10 ]
    n              = int ( n / 10 )
  return sumOfSquares

def chainDigits ( n ) :
  if numbers [ n ] == -1 :
    return False
  if numbers [ n ] == 1 :
    return True
  #print ( n )
  if chainDigits ( squareOfDigits ( n ) ) :
    numbers [ n ] = 1
    return True
  else :
    numbers [ n ] = -1
    return False

success = 0

for i in range ( 2, 10000001 ) :
  n = i
  if i > 567 :
    n = squareOfDigits ( i )
  if chainDigits ( n ) :
    success += 1

elapsed = ( time.perf_counter() - start )

print ( "The number of chains that end in 89 is " + str ( success ) )

print ( "Calculated in: " + str ( elapsed ) + " seconds." )
