#Assignment Information
print("Programming Assignment #1")

#Function to solve sample mean
def sampleMean(sm, num, sof, n):
  mean = sof/n
  sampleMean = sm + ((mean-sm)/n)
  return sampleMean

def sampleVariance(sv, num, sof, n):
  mean = sof/n
  if(n>1):
    pMean = (sof-num)/(n-1)
  else:
    pMean = 0
  if(n>1):
    res = (((n-2)/(n-1))*(sv)) + ((pow((mean-pMean),2))/n)
  else:
    res = 0
  return res

#Array to store Numbers
num = int(input("Enter Non-Negative number to calculate Mean and Variance : "))

sumOfNumbers = 0 # Sum of numbers
sm = 0 # -> Sample Mean
n=0  # -> Number of values entered by users
sv = 0 # -> Sample Variance

while(num >=0 ):
  n += 1
  sumOfNumbers += num
  sm = sampleMean(sm, num, sumOfNumbers, n)
  sv = sampleVariance(sv, num, sumOfNumbers, n)
  print(sm , "======> Sample Mean")
  print(sv , "======> Sample Variance")
  num = int(input("Enter Non-Negative number to calculate Mean and Variance : "))