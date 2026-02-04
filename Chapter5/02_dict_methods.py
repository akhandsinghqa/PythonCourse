# Dictonary Methods

a = {
    "name": "akhand",
    "from": "india",
    "marks": [92, 98, 96],
    1: "demo"
}

# print(a.keys())
# print(a.values())
# print(a.items())
# a.update({"name":"pratap","add":"added"})
# print(a.items())
# print(a.get("marks"))

for key, value in a.items():
    print(key, value)

d = {x ** 2 for x in range(10)}
print(d)
