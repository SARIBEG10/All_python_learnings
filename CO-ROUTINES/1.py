def searching(string):
    print("searching string is : {} ".format(string))
    try:
        while True:
            name = yield
            if string in name:
                print(name)
    except GeneratorExit:
        print("Closing Coroutine")


x = searching("saribeg")
x.__next__()

x.send("hello")
x.send("hello saribeg")
x.close()
x.send("send some data")




