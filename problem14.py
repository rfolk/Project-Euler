# Russell Folk
# July 9, 2013
# Project Euler #14
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

import time

chains  = []
ceiling = 1000001

head    = -1
length  = -1

def nextChain ( n ) :
  if n == 1 :
    return 1
  if n < 3 * ceiling and chains [ n ] != 0 :
    return chains [ n ] + 1
  current = -1
  if n % 2 == 0 :
    current = nextChain ( int ( n / 2 ) )
  else :
    current = nextChain ( 3 * n + 1 )
  if n < 3 * ceiling :
    chains [ n ] = current + 1
    return chains [ n ]
  else :
    return current + 1

start = time.perf_counter()

# This will initialize found chains from any location to 0
for i in range ( 3 * ceiling ) :
  chains.append ( 0 )

chains [ 1 ] = 1

for i in range ( 2 , ceiling , 1 ) :
  thisHead    = i
  thisLength  =  nextChain ( i )

  #if chains [ thisHead ] == 0 :
  #  chains [ thisHead ] == thisLength
  if thisLength > length :
    length  = thisLength
    head    = thisHead
  #print ( "Working on: " + str ( i ) )

elapsed = ( time.perf_counter() - start )

print ( "The starting number that produces the longest chain is " +
  str ( head ) + " with a chain of " + str ( length ) )

print ( "Calculated in: " + str ( elapsed ) + " seconds." )
