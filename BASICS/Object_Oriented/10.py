"""(INSTANCE , STATIC, CLASS) METHODS"""


class my_class(object):

    def __init__(self):
        print("this is constructor method")

    def instance_method(self):
        print("this method is instance method and need object(instance)")

    @staticmethod
    def static_method(name):
        print("this is static method")
        print("hello {}".format(name))

    @classmethod
    def class_method(cls):
        cls.static_method("Saribeg")


if __name__ == "__main__":

    new_object = my_class()
    new_object.instance_method()
    new_object.static_method("saribeg")
    new_object.class_method()

