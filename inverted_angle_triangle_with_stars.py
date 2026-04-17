# print pattern >> inverted angle triangle with stars:
# *****
# ****
# ***
# **
# *

user_input = int(input("Enter the number to display inverted triangle number of times: "))

for i in range(user_input, 0, -1):
  print("*"*i)
