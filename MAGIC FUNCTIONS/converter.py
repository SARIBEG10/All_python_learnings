class Length_Converter:
    value = {'cm': 0.01, 'mm': 0.001, 'km': 1000, 'm': 1}

    def __init__(self, value, value_unit='m'):
        self.value = value
        self.value_unit = value_unit

    def Convert_meters(self):
        return self.value * Length_Converter.value[self.value_unit]

    def __add__(self, other):
        ans = self.Convert_meters() + other.Convert_meters()
        return Length_Converter(ans/Length_Converter.value[self.value_unit], self.value_unit)

    def __str__(self):
        return str(self.Convert_meters)

    def __repr__(self):
        return "Length Conversion " + str(self.value) + " , " + self.value_unit


if __name__ == "__main__":

    obj1 = Length_Converter(5, 'cm')
    obj2 = Length_Converter(6, 'km')
    print(repr(obj1 + obj2))
    # print(obj1.Convert_meters())