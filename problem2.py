#! /usr/bin/env python3.3

# Russell Folk
# November 29, 2012
# Project Euler #2
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

stop        = 4000000
total       = 0
currentTerm = 1
nextTerm    = 1

while currentTerm < stop :
  if ( currentTerm % 2 == 0 ) :
    total += currentTerm
  tempTerm    = currentTerm + nextTerm
  currentTerm = nextTerm
  nextTerm    = tempTerm

print ( "The sum of the even numbered terms in the Fibonacci sequence below "
        + str ( stop ) + " is: " + str ( total ) )
