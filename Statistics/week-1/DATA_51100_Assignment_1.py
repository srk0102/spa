#Assignment Information
print("Data 51100- Summer 2021")
print("Sam Abuomar")
print("Programming Assignment #1")

#Setting up format strings
fs = 'Mean is %.2f and Variance is %.6f'
fs1 = 'Mean is %.2f and Variance is 0'

#Create Empty List
numbers = []

#Importing Variance from Stats
from statistics import variance

#Asking for the user input

num = int(input("Enter a number: "))

#Adding the number to the empty list
numbers.append(num)

#Printing info for the first number
x = num
print(fs1 % (x))

#Setting up loop
num = int(input("Enter a number: "))
while num >=0:
    numbers.append(num)
    
    #Mean formula
    x = sum(numbers) / len(numbers)
    
    #Variance formula
    y = variance (numbers)
    
    #Printing Info for the rest of numbers
    print (fs % (x, y))
    num = int(input("Enter a number: "))
    
    if num == "q":
        break