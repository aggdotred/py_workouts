


def mysum(*args):
    acc = 0
    for i in args:
        acc += i
    return acc


print(mysum(1))

print(mysum(1, 2))

print(mysum(1, 2, 3))
