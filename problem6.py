#! /usr/bin/env python3.3

import time

# Russell Folk
# November 30, 2012
# Project Euler #6
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

squares = 0
sums    = 0

start = time.perf_counter()

for i in range ( 1 , 101 ) : # 1 greater than the stopping point
  squares += i ** 2
  sums    += i
sums    = sums ** 2
answer  = sums - squares

elapsed = ( time.perf_counter() - start )

print ( "The difference between the square of sums and the sum of squares 1" +
        " to 20 is " + str ( answer ) )

print ( "Calculated in: " + str ( elapsed ) + " seconds." )
