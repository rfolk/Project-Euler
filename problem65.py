#! /usr/bin/env python3.3

# Russell Folk
# December 3, 2012
# Project Euler #65
# http://projecteuler.net/problem=65


import time

limit = 100

def digitSum ( n ) :
  """
    Adds the sum of the digits in a given number 'n'
  """
  return sum ( map ( int , str ( n ) ) )

def calceNumerator ( term , numeratorN1 , numeratorN2 ) :
  """
    Calculates the numerator of e to the required term
  """
  if term == limit :
    if term % 3 == 0 :
      return ( 2 * int ( term / 3 ) * numeratorN1 ) + numeratorN2
    return numeratorN1 + numeratorN2

  multiplier  = 1
  if term % 3 == 0 :
    multiplier = 2 * int ( term / 3 )
  numerator   = multiplier * numeratorN1 + numeratorN2

  return calceNumerator ( term + 1 , numerator , numeratorN1 )

start   = time.perf_counter()

number  = calceNumerator ( 2 , 2 , 1 )
total   = digitSum ( number )

elapsed = ( time.perf_counter() - start )

print ( "The digit sum of the numerator of the 100th convergent of e is: " +
        str ( total ) + "." )

print ( "Calculated in: " + str ( elapsed ) + " seconds." )
