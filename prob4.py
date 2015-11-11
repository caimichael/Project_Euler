# coding=utf-8
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#Decrement from 999 * 999 to 999 * 998 ...
#for each of product:
#    invert = invert the digits
#    if invert = original:
#        print invert
#        break

palin_list = []
for num1 in xrange(999,0,-1):
    for num2 in xrange(999,0,-1):
        product = num1*num2
        if str(product) == str(product)[::-1]:
            palin_list.append(product)

palin_list.sort(reverse=True)
print palin_list[0]
