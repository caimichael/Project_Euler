# coding=utf-8

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#
#20 (4*5,2*10)
#19
#18 (2*9,3*6)
#17
#16 (4*4,2*8)
#15 (3*5)
#14 (2*7) 1 2 3 4 5 6 7 8 9 10
#13
#12 (2*6,3*4)
#11
#Only need to test if its divisible by 11-20 (and it will also be divisible by 1-10)

for number in xrange(1,10000000000):
    if (number % 11 == 0 and number % 12 == 0 and number % 13 == 0 and number % 14 == 0
    and number % 15 == 0 and number % 16 == 0 and number % 17 == 0 and number % 18 == 0
    and number % 19 == 0 and number % 20 == 0):
        print number
        break

#for number in xrange(1,10000):
#    if (number % 3 == 0 and number % 5 == 0 and number % 6 == 0
#            and number % 7 == 0 and number %  8 == 0 and number % 9 == 0 and number % 10 == 0):
#        print number
#        break

