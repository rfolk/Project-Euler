#! /usr/bin/env python3.3

import time

# Russell Folk
# November 30, 2012
# July 9, 2013 — Optimized
# Project Euler #5
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

def isDivisible ( n ) :
  '''
    Checks if the number n is evenly divisible by every number < 20
  '''
  start = 1
  stop  = 21 # one greater so that the range is correct
  for i in range ( start , stop ) :
    if ( n % i != 0 ) :
      return False
  return True

check   = False
number  = 0

start = time.perf_counter()

while not check :
  number  += 380  # 380 is the least common multiple of 19 and 20.
  check    = isDivisible ( number )

elapsed = ( time.perf_counter() - start )

print ( "The smallest number evenly divisible by 1-20 is " +
        str ( number ) + "." )

print ( "Calculated in: " + str ( elapsed ) + " seconds." )
