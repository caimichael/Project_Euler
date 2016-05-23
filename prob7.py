#By listing the first six prime numbers:
#    2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

import numpy as np

# def find_prime(n):
#     counter = 1 #accounting for 2 being the first prime
#     for num in np.arange(3,1e10):
#         for i,less_num in enumerate(np.arange(2,sqrt(num)+1))[1::2]:
#             if num % less_num == 0:
#                 break
#             if i == len(np.arange(2,sqrt(num)+1)[1::2]) - 1:
#                 counter +=1
#         if counter == n:
#             return num
#
# print find_prime(100)

#Sieve method

def find_prime(n):
    counter = 0
    isprime = [True for _ in np.arange(int(1e7))]
    for i in np.arange(2,int(1e7)):
        if isprime[i] == False:
            continue
        for j in np.arange(2*i,int(1e7), i):
            isprime[j] = False
        counter+=1 
        if counter == n:
            return i

print(find_prime(10001))
