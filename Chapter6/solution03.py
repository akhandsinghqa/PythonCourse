# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams

p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

comment = input("Please leave your comment: ")

# if (
#     comment.find("Make a lot of money") >= 0
#     or comment.find("buy now") >= 0
#     or comment.find("subscribe this") >= 0
#     or comment.find("click this") >= 0
# ):
#     print("This comment is marked as spam.")
# else:
#     print("This is not spam")

if (p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print("This comment is marked as spam.")
else:
    print("This is not spam")
print(("End of program"))
