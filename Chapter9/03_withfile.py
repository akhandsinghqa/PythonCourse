# Use of with function to read and write the file.
with open("newfile.txt", "r") as f:
    text = f.read()

print(text)
