from math_1 import Math

test_mat = Math()

def test_add(a,b):
  print(test_mat.add(a,b))

def test_multiply(a,b):
  print(test_mat.multiply(a,b))

def test_divide(a,b):
  print(test_mat.divide(a,b))

def test_is_even(a):
  print(test_mat.is_even(a))

def test_power(a,b):
  print(test_mat.power(a,b))

def test_is_prime(a):
  print(test_mat.is_prime(a))

def test_factorial(a):
  print(test_mat.factorial(a))

def test_factors(a):
  print(test_mat.factors(a))

test_add(24,54) # testing addition with 24,54 result = 78
test_multiply(2,8) # testing multiply with 2,8 result = 16
test_divide(44,2) # testing divide with 44,2 result = 22.0
test_is_even(6) # testing is_even with 8 result = False * Wrong OutPut * Expected Output - True
test_power(4,2) # testing power with 4,2 result = 16
test_is_prime(6) # testing is_prime with 8 result = False
test_factorial(5) # testing factorial with 5 result = 24 * Wrong OutPut * Expected Output - 120
test_factors(9) # testing factors with 9 result = TypeError: factors() takes 1 positional argument but 2 were given * Wrong OutPut * Expected Output - [1,3,9]