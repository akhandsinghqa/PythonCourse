values = ["Akhand", 27,67.89, True,None,"Demo"]
print(values)
print(values.index(67.89))
print(values.count("added"))
values.append("added")
print(values.count("added"))
values.reverse()
values.insert(4,"inserted")
values.pop(2)
values.remove(True)
print(values)

l1=[2,6,1,97,34,456,5]
l1.sort()
print(l1)

lst = [1, 2]
print(lst)
lst.append(3)
# lst.append([4, 5])  [1, 2, 3, [4, 5]]
print(lst)
lst.extend([4, 5])
print(lst)
lst.pop()   # 5
print(lst)
lst.pop()   
print(lst)
lst.clear()
print(lst)
