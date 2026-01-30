# Write a program to find out whether a given post is talking about "Akhand" or not.

post = input("Please post about program : ")

if "Akhand".lower() in post.lower():
    print("Post is talking about Akhand.")
else:
    print("Post not talking about Akhand")

print("End of Program.")
