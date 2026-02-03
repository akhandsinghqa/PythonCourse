# Write into file

st = "This file created using write function."
f = open("myfile.txt", "w")
f.write(st)
f.close()

af = open("myfile.txt", "a")
af.write("\nThis line is added using append.")
af.close()

rf = open("myfile.txt")
print(rf.read())
rf.close()
