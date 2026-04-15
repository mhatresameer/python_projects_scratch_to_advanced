# user input to check largest of two numbers

number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))

# check conditions with if-else
if number_one > number_two:
  print(f"{number_one} is largest of two numbers.")
else:
  print(f"{number_two} is the largest of two numbers.")
