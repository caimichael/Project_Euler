# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
from math import sqrt

pfact = 1
for x in xrange(2,int(sqrt(600851475143))):
  if 600851475143 % x == 0: #means that x is a divisor
    isPrime = True
    for y in xrange(2,x): #checking to see if x is prime (for non 1 or x divisors)
      if x % y == 0: #this means that it is not prime
        isPrime = False
        break
    if isPrime:
      pfact = x

print pfact