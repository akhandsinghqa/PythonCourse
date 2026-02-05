from functools import reduce

print("*************** Map Usage ***********************")


def sqrs(num):
    return num ** 2


result_two = map(sqrs, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print([i for i in result_two])
print(list(result_two))

result = map(lambda x: x * "a", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print([i for i in result])
print(list(result))

print("*************** Filter Usage ***********************")
lsts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def less_5(num):
    if num < 5:
        return True
    else:
        return False


print([i for i in filter(less_5, lsts)])
print(list(filter(less_5, lsts)))

print([i for i in filter(lambda x: x > 5, lsts)])
print(list(filter(lambda x: x > 5, lsts)))

print("*************** Reduce Usage ***********************")


def sum_num(a, b):
    return a + b


print(reduce(sum_num, lsts))

print(reduce(lambda x, y: x * y, lsts))
