# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.

try:
    with (open("first.txt") as f, open("second.txt") as s, open("third.txt") as t):
        f.read()
        s.read()
        t.read()
except FileNotFoundError as error:
    print(error)
