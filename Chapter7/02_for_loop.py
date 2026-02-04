# For Loop

for i in range(1, 11):
    print(i)

for i in range(1, 50, 5):
    print(i)

name = "Akhand"

for i in name:
    print(i)

tpl = (1, 2, 3, 4, 5)
for j in tpl:
    print(j)

d = {"name": "Akhand", "place": "Bharat", "time": "2026"}

for k in d:
    print(k)

# Break in loop

for i in range(80):
    if (i == 5):
        break
    print(i)

for i in range(80):
    if (i == 5):
        continue
    print(i)

for i in range(80):
    pass
