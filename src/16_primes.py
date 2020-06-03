import sys
import math

# my shot at finding primes. works for anything that is a multiple of these primes. breaks at 23x23, or past 529
#how to see if something is a prime number.
# a prime number is something that can only be divided evenly by itself and 1
# all numbers can be described as primes multiplied as components
# so I was going to see what can evenly be divided by prime numbers, that are not themselves

#were taking in a single number to evaluate
# num=int(sys.argv[1])

# #a short list of primes as components
# primes=[2,3,5,7,11,13,17,19]
# #a flag to trigger if it's prime not prime
# flag=False

# #a loop to look through the primes
# for prime in primes:
#     #check if it is one of the primes in out list, or divisable by them
#     if (num != prime and num % prime == 0):
#         flag=True
#         print(f"{num} is not prime")
#         break

# if(not flag):
#     print(f"{num} is prime")


#implimenting Sieve of Eratosthenes

#this stays the same as it is our input
num=int(sys.argv[1])
print(num)

def generate_primes(n):
    n=n*2
    table = [True for x in range(n)]
    for i in range (2, int(math.sqrt(n))):
        if table[i]:
            for j in range(i*2, n, i):
                table[j] = False
    #we store the table as a set for O(1) searches
    primes={x for x in range(len(table)) if table[x] == True} #return primes when activated primes
    return primes
    # return table

def is_prime(n):
    return n in primes

primes = generate_primes(num)
# print(primes)
print(f"{num}, {is_prime(num)}")

#extra notes
# import math
# A simple implementation of the Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Key limitation: The Sieve of Eratosthenes has a memory complexity of O(n), where n is the size of the prime number.
# O(n * log(log(n))) (the reasoning why is quite complex, see the wiki article).


# def generate_primes(n):
#     table = [True for x in range(n)]
#     for i in range (2, int(math.sqrt(n))):
#         if table[i]:
#             for j in range(i*2, n, i):
#                 table[j] = False

#     # Return a dict to make searches an O(1) operation.
#     primes = {x for x in range(len(table)) if table[x] == True}
#     return primes

# def is_prime(n):
#     return n in primes

# primes = generate_primes(100)
# # Anything larger than 8 digits begins to take a very long time to generate.

# print(primes)

# print(f"0 {is_prime(0)}")
# print(f"1 {is_prime(1)}")
# print(f"2 {is_prime(2)}")
# print(f"17 {is_prime(17)}")

# print(f"4 {is_prime(4)}")
# print(f"10 {is_prime(10)}")
# primes = generate_primes(num)

# print(primes)
# print(f"{num},{is_prime(num)}")