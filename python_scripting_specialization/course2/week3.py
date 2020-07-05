# my_list = [1, 3, 5, 7, 9]
# print(my_list[2:])
#
# a = ([1])
# print(type(a))
#
# instructors = ("Scott", "Joe", "John", "Stephen")
# instructors[2 : 4] = []
# print(instructors)

# my_list = [1, 3, 5, 7, 9]
# my_list.reverse()
# print(my_list.reverse())
#
# fib = [0,1]
# n = int(input("Enter value of n : "))
# for i in range(0,n):
#     a = fib[-1]
#     b = fib[-2]
#     c = a+b
#     fib.append(c)
# print(fib)
#

"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

import math

print ("Enter the a number")
number = int(input())

primes = []
for i in range(2,number+1):
    primes.append(i)

i = 2
#from 2 to sqrt(number)
while(i <= int(math.sqrt(number))):
    #if i is in list
    #then we gotta delete its multiples
    if i in primes:
        #j will give multiples of i,
        #starting from 2*i
        for j in range(i*2, number+1, i):
            if j in primes:
                #deleting the multiple if found in list
                primes.remove(j)
    i = i+1

print (primes)
print(len(primes))
