
class MyVector:
    def _init_(self, *vect):
        self.vect = vect
        if len(self.vect) != 0:
            for x in self.vect:
                if not type(x) is int:
                    raise ValueError("Invalid Argument passed.")

    def __repr__(self) -> str:
        return "MyVector()"

    def __str__(self) -> str:
        return f"MyVector{self.vect}"

    def __len__(self):
        return len(self.vect)

    def __iter__(self):
        return (x for x in self.vect)

    def __setitem__(self, index, value):
        self.vect = list(self.vect)
        self.vect[index] = value
        self.vect = tuple(self.vect)

    def __getitem__(self, i):
        try:
            return self.vect[i]
        except IndexError:
            print("Index out of Range!")

    def __abs__(self):
        res = 0
        for i in range(0, len(self.vect)):
            res = res + self.vect[i] ** 2
        return float(res ** 0.5)


    def __bool__(self):
        if abs == 0:
            return False
        else:
            return True

# ///////////////////////// Arithmetic ////////////////////////////////

    def __add__(self, other):
        return f"MyVector{tuple(map(sum, zip(self.vect, other.vect)))}"

    def __mul__(self, other):
        self_vectors = list(self.vect)
        for i in range(0, len(self_vectors)):
            self_vectors[i] = self_vectors[i] * other
        return f"MyVector{tuple(self_vectors)}"

    def __rmul__(self, other):
        self_vectors = list(self.vect)
        for i in range(0, len(self_vectors)):
            self_vectors[i] = self_vectors[i] * other
        return f"MyVector{tuple(self_vectors)}"

    def __lshift__(self, val):
        temp = list(self.vect)
        temp = temp[val:] + temp[:val]
        self.vect = tuple(temp)
        del temp
        return f"MyVector{self.vect}"
