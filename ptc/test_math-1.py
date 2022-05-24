from math_1 import Math

test_mat = Math()

print(test_mat.add(8,5)) # testing addition with 8,5 result = 13

print(test_mat.multiply(8,5)) # testing multiply with 8,5 result = 40

print(test_mat.divide(8,5)) # testing divide with 8,5 result = 1.6

print(test_mat.is_even(8)) # testing is_even with 8 result = False # Wrong OutPut # Expected Output - True

print(test_mat.power(8,5)) # testing power with 8,5 result = 32768

print(test_mat.is_prime(8)) # testing is_prime with 8 result = False

print(test_mat.factorial(5)) # testing factorial with 5 result = 24 # Wrong OutPut # Expected Output - 120

print(test_mat.factors(16)) # testing factors with 16 result = TypeError: factors() takes 1 positional argument but 2 were given # Wrong OutPut * Expected Output - [1,2,4,8,16]