#! /usr/bin/env python3.3

# Russell Folk
# December 3, 2012
# July 9, 2013 — Optimized
# Project Euler #10
# Find the sum of all the primes below two million.

def isPrime ( n ) :
  x = int ( n ** 0.5 )
  if n % 2 == 0 :
    return False
  for i in range ( 3 , x + 1 , 2 ) :
    if n % i == 0 :
      return False
  return True

end   = 2000000
total = 2

for n in range ( 3 , end , 2 ) :
  if isPrime ( n ) :
    total += n

print ( "The total of all the primes below " + str ( end ) + " is "
  + str ( total ) )
