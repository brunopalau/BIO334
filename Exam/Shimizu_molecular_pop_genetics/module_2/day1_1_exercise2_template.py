import math

list1 = [1, 2, 3, 4, 5, 6]


# YOUR CODE HERE
summe = 0
for ele in list1:
    summe += ele
mean = summe/len(list1)

sum_resid = 0
for ele in list1:
    sum_resid += (mean-ele)**2
sd = math.sqrt(sum_resid/len(list1))



print("list = ", list1)
print("sd = %f" % sd)

