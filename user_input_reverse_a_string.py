# Reverse a string using loop
reverse_string_input = input("Enter a string to reverse it: ")
dummy_variable = ""

for char in reverse_string_input:
  dummy_variable = char + dummy_variable

print(dummy_variable)
