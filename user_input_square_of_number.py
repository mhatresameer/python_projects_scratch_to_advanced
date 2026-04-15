# Ask user a number and print:
# 1 → Square = 1
# 2 → Square = 4
# 3 → Square = 9
user_square_check = int(input("Enter the number to square it: "))

# i is a temporary variable
for i in range(1, user_square_check+1):
  print(i, "> Square =", i*i)

# the flow goes like:
# user_square_check = 3
# i = (not created yet)

# loop starts - iteration 1
# i = 1
# user_square_check = 3
# i * i = 1 * 1 = 1
# 1 → Square = 1

# loop starts again - iteration 2
# i = 2
# user_square_check = 3
# 2 * 2 = 4
# 2 → Square = 4

# loop starts again - iteration 3
# i = 3
# user_square_check = 3
# 3 * 3 = 9
# 3 → Square = 9

# i tries to go to number 4 (stops because range is till what user has entered the input value)
