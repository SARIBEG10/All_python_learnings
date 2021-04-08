x = 10


def foo():
    global x
    x = 20
    return x


print(foo())
help(foo())
print(dir(foo()))
print(foo().__doc__)