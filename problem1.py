#! /usr/bin/env python3.3

# Russell Folk
# November 29, 2012
# Project Euler #1
# Find the sum of all the multiples of 3 or 5 below 1000.

# stop is 990 because the cycle will not complete before 1000.
stop   = 990

total = 0
count = 0

# Could be done with mod 3 and 5 but will be less efficient
while count < stop :
  count += 3
  total += count
  count += 2
  total += count
  count += 1
  total += count
  count += 3
  total += count
  count += 1
  total += count
  count += 2
  total += count
  count += 3
  total += count

count += 3
total += count
count += 2
total += count
count += 1
total += count
count += 3
total += count

print ( "The total of all the multiples of 3 and 5 added together is: "
  + str ( total ) )
