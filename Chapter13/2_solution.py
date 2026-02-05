# A list contains the multiplication table of 7. write a program to convert it to vertical
# string of same numbers.

# print(filter(lambda x:x+"\n",[17*i for i in range(1,11)]))
for i in range(1, 20):
    table = [str(i * j) for j in range(1, 11)]
    print("\n".join(table))
