#coding = utf-8

#Find the difference between the sum of the squares of the first
#one hundred natural numbers and the square of the sum.

numsum = 0
list_sq = []
for num in xrange(1,101):
    numsum = numsum + num
    numsq = num**2
    list_sq.append(numsq)

sum_list_sq = sum(list_sq)
sq_sum = numsum**2

print sq_sum - sum_list_sq
