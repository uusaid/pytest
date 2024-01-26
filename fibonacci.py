print("Fibonacci series")

num1 = 0
num2 = 1
counter = 0
print(num1)
print(num2)
while counter < 100:
  num3 = num1 + num2
  print(num3)
  num1 = num2
  num2 = num3
 
  counter += 1