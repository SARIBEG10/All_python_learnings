class Dictionary(dict):

    def __add__(self, other):
        self.update(other)
        return Dictionary(self)


if __name__ == "__main__":
    dict1 = {'firstname': 'Saribeg'}
    dict2 = {'lastname': 'Farmanian'}
    obj1 = Dictionary(dict1)
    obj2 = Dictionary(dict2)
    print(obj1 + obj2)













