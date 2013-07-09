#! /usr/bin/env python3.3

# Russell Folk
# November 29, 2012
# Project Euler #3
# What is the largest prime factor of the number 600851475143?

def isPrime ( n ) :
  '''
    Returns true if the number n is prime else false
  '''
  if ( n % 2 == 0 ) :
    return False
  for i in range ( 3 , n - 1 , 2 ) :
    if ( n % i == 0 ) :
      return False
  return True

goal  = 600851475143
stop  = int ( goal ** 0.5 )
prime = 2

for n in range ( 3 , stop , 2 ) :
  if goal % n == 0 :
    if isPrime ( n ) :
      prime = n

print ( "The largest prime multiple of " + str ( goal ) + " is "
        + str ( prime ) + ".")
