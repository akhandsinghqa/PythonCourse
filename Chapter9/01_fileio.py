# open() function for file
f = open("newfile.txt")
lines = f.readlines()
f.seek(0)  # This rewinds the file to start
line = f.readline()
f.seek(0)  # This rewinds the file to start
text = f.read()
print(lines, type(lines))
print(line, type(line))
print(text, type(text))
f.close()
