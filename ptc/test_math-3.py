from math_1 import Math

test_mat = Math()

print(test_mat.add(99,6)) # testing addition with 99,6 result = 105

print(test_mat.multiply(99,6)) # testing multiply with 99,6 result = 594

print(test_mat.divide(99,6)) # testing divide with 99,6 result = 16.5

print(test_mat.is_even(99)) # testing is_even with 99 result = False

print(test_mat.power(99,6)) # testing power with 99,6 result = 941480149401

print(test_mat.is_prime(99)) # testing is_prime with 99 result = False

print(test_mat.factorial(6)) # testing factorial with 6 result = 120 # Wrong OutPut # Expected Output - 720

print(test_mat.factors(16)) # testing factors with 16 result = TypeError: factors() takes 1 positional argument but 2 were given # Wrong OutPut * Expected Output - [1,2,4,8,16]