# def tables(num:int):
#     print([num*i for i in range(1,11)])
# for i in range(1,21):
#     tables(i)

a_lst = [5, 6, 7, 8, 9, 12, 3, 45, 23, 788, 7, 23, 76]
print(a_lst)
b_lst = [i for i in a_lst if i > 10]
print(b_lst)
c_lst = [i for i in a_lst if i < 10]
print(c_lst)
