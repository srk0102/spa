import math
class shapes:
  # def __init__(self, length, height):
  #   self.length = length
  #   self.height = height
  
  def rectangle(self, length, height):
    area = length * height
    permiter = (2 * (length + height))
    return [area,permiter]
  
  def square(self, length):
    area = pow(length, 2)
    permiter = 4 * length
    return [area,permiter]
  
  def triangle(self, length, height):
    area = (length*height)/2
    hypotenuse = (math.sqrt(pow(length,2)+pow(height,2)))
    permiter = (length+height+hypotenuse)
    return [area,permiter]

findPA = shapes()
print(findPA.rectangle(5,4), "===========> RECTANGLE")
print(findPA.square(5), "===========> SQUARE")
print(findPA.triangle(5,4), "===========> TRIANGLE")