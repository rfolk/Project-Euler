#! /usr/bin/env python3.3

# Russell Folk
# November 30, 2012
# July 9, 2013 — Optimized
# Project Euler #4
# Find the largest palindrome made from the product of two 3-digit numbers.

import time

def isPalindrome ( n ) :
  '''
    Reverses the number then tests whether or not the number is the same.
  '''
  original    = n
  palindrome  = 0
  while original > 0 :
    digit       = original % 10
    palindrome  = palindrome * 10 + digit
    original    = int ( original / 10 )
  return ( palindrome == n )

value1 = value2 = 99
palindrome = 0

start = time.perf_counter()

for i in range ( 999 , 99 , -1 ) :
  if i < value1 and i < value2 :
    break
  for j in range ( 999 , 99 , -1 ) :
    if j < value1 and j < value2 :
      break
    if ( i * j ) > palindrome :
      if isPalindrome ( i * j ) :
        palindrome = i * j
        value1 = i
        value2 = j

elapsed = ( time.perf_counter() - start )

print ( "The largest palindrome from 2 three digit numbers is: " +
        str ( palindrome ) + " = " + str ( value1 ) + " * " +
        str ( value2 ) + "." )

print ( "Calculated in: " + str ( elapsed ) + " seconds." )
