def x(sentence, next_coroutine):
    y = sentence.split(" ")
    for z in y:
        next_coroutine.send(z)
    next_coroutine.close()


def w(pattern="Alenoush", next_coroutine=None):
    print("Searching string is : {} ".format(pattern))
    try:
        while True:
            z = yield
            if pattern in z:
                next_coroutine.send(z)
    except GeneratorExit:
        print("matching is Done")


def printing():
    try:
        while True:
            z = yield
            print(z)
    except GeneratorExit:
        print("End of pipelining")


p = printing()
p.__next__()

f = w(next_coroutine=p)
f.__next__()

sentenc = "I have a great relationship with Alenoush"
x(sentenc, f)





