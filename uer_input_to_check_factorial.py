# Find factorial of a number
factorial_input = int(input("Enter the number to check factorial of the same: "))
count = 1

for i in range(1, factorial_input + 1):
  count *= i

print ("The factorial of",factorial_input," is",count)
