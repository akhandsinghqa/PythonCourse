# Write a program to detect double space in a string.

line="This is double  line for testing."

print(line)
print(line.find("  "))

# Replace the double space from problem 3 with single spaces.
print(line.replace("  "," "))