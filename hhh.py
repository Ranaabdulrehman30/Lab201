import math
class MyVector:

    def __init__(self, *arb):
        try:
            self.a = int(a)
            self.b = int(b)
            self.c = int(c)
            self.wrapped = [a, b, c]
        except ValueError:
            print("In valid Argument name")

    def __str__(self):
        return "({0}, {1}, {2})".format(self.a, self.b, self.c)

    def __len__(self):
        return len(self.wrapped)

    def __setitem__(self, key, value):
        if key == 0:
            self.a = value
        if key == 1:
            self.b = value
        else:
            self.c = value

    def __getitem__(self, subscript):
        return self.wrapped[subscript]

    def __abs__(self):
        absolute = (math.pow(self.a, 2) + math.pow(self.b, 2) + math.pow(self.c, 2))
        return int(math.pow(absolute, 0.5))

    def __bool__(self):
        absolute = (math.pow(self.a, 2) + math.pow(self.b, 2) + math.pow(self.c, 2))
        if absolute == 0:
            return False
        else:
            return True

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        return MyVector(a, b, c)

    def __mul__(self, other):
        a = self.a*other
        b = self.b * other
        c = self.c * other
        return MyVector(a, b, c)

    def __rmul__(self, other):
        return MyVector(self.a*other, self.b*other, self.c*other)

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x < 3:
            element = self.wrapped[self.x]
            self.x += 1
            return element
        else:
            raise StopIteration

    def __lshift__(self, other):
        if other == 1:
            return self.b, self.c, self.a
        if other == 2:
            return self.c, self.b, self.a
        else:
            return self.a, self.b, self.c





if __name__ == '__main__':
    v0 = MyVector(2, 3, 5)
    print(v0)
    v1 = MyVector(3, 5, 99)
    print(len(v1))

    for elem in v1:
        print(elem)

    print(v1[2])
    v1[2] = 33
    print(v1)

    v2 = MyVector(3, 4, 2)

    print(abs(v2))

    if v0:  # True
        print("this line will print")
    if v1:  # True
        print("this line will NOT print")

######### Arithmetic #############

    x1 = MyVector(1, 2, 3)
    x2 = MyVector(4, 5, 6)
    x3 = x1 + x2
    print(x1)
    print(x2)
    print(x3)
    v1 += v2
    print(v1)
    print(v2)
    x1 = MyVector(1, 2, 3)
    x2 = x1*3
    x3 = 3*x1
    print(x1)
    print(x2)
    print(x3)


    x4 = x3 << 1
    print(x4)