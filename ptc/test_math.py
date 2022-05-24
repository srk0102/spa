from math_1 import Math

mat = Math()

print(mat.add(2,3)) # testing addition with 2,3 result = 5

print(mat.multiply(2,3)) # testing multiply with 2,3 result = 6

print(mat.divide(2,3)) # testing divide with 2,3 result = 0.6666

print(mat.is_even(2)) # testing is_even with 2 result = False ----> Wrong OutPut -----> Expected Output - True

print(mat.power(2,3)) # testing power with 2,3 result = 8

print(mat.is_prime(2)) # testing is_prime with 2 result = True

print(mat.factorial(3)) # testing factorial with 3 result = 2 ------> Wrong OutPut -----> Expected Output - 6

print(mat.factors(4)) # testing factors with 4 result = TypeError: factors() takes 1 positional argument but 2 were given ----> Wrong OutPut -----> Expected Output - [1,2,4]