#Assignment Information
print("Programming Assignment #1")

#Function to solve sample mean
def sampleMean(sm, num, sof, n):
  mean = sof/n
  if(n>1):
    pMean = (sof-num)/(n-1)
  else:
    pMean = 0
  sampleMean = pMean + ((mean-pMean)/n)
  return sampleMean

#Array to store Numbers
num = int(input("Enter Non-Negative number to calculate Mean and Variance : "))

sumOfNumbers = 0 # Sum of numbers
sm = 0 # -> Sample Mean
n=0  # -> Number of values entered by users

while(num >=0 ):
  n += 1
  sumOfNumbers += num
  sm = sampleMean(sm, num, sumOfNumbers, n)
  print(sm)
  num = int(input("Enter Non-Negative number to calculate Mean and Variance : "))