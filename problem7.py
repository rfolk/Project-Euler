#! /usr/bin/env python3.3

# Russell Folk
# December 2, 2012
# Project Euler #7
# July 9, 2013 — Optimized
# What is the 10,001st prime number?

def isPrime ( n ) :
  x = int ( n ** 0.5 )
  for i in range ( 2 , x + 1 ) :
    if ( n % i == 0 ) :
      return False
  return True

stop  = 10001
prime = 0     # initialized to 0
n     = 3     # we know that 1, 2, and 3 are prime numbers
i     = 3     # starting at 3 so that we can increment by 2

while n <= stop :
  i += 2      # primes must be odd
  if isPrime ( i ) :
    prime  = i
    n     += 1

print ( "The " + str ( stop ) + "th prime number is " + str ( prime ) + "." )