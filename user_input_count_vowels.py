# Count vowels in a word:

word = input("Enter word to check vowels: ")
count = 0

for char in word:
    if char.lower() in "aeiou":
        count += 1

print("Vowels found are:", count)

# user entered "Sameer" in this case:
# iteration 1 -
# char = 'S'
# is 'S' in "aeiou"? No
# count = 0

# iteration 2 -
# char = 'a'
# is 'a' in "aeiou"? Yes
# count = 1

# iteration 3 -
# char = 'm'
# is 'm' in "aeiou"? No
# count = 1

# iteration 4 -
# char = 'e'
# is 'e' in "aeiou"? Yes
# count = 2

# iteration 5 -
# char = 'e'
# is 'e' in "aeiou"? Yes
# count = 3

# iteration 5 -
# char = 'r'
# is 'r' in "aeiou"? No
# count = 3
