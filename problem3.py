#! /usr/bin/env python3.3

# Russell Folk
# November 29, 2012
# Project Euler #3
# What is the largest prime factor of the number 600851475143?

def isPrime ( n ) :
  '''
    Returns true if the number n is prime else false
  '''
  for i in range ( 2 , n - 1 ) :
    if ( n % i == 0 ) :
      return False
  return True

goal  = 600851475143
stop  = int ( goal ** 0.5 )
prime = 2

for n in range ( 2 , stop ) :
  if goal % n == 0 :
    if isPrime ( n ) :
      prime = n

print ( "The largest prime multiple of " + str ( goal ) + " is "
        + str ( prime ) + ".")
