# String Slicing
name="Akhand"

shortname=name[0:3]
print(shortname)

print(name[2:3])
print(name[0:4])

print(name[:4])
print(name[2:])

print(name[0:5:2]) # Jump to 2nd char

# Negative Slicing

print(name[-4:-1])
print(name[-1:-4:-1]) # Jump back by 1 char

print(name[:-4])

print(name[::-1])
