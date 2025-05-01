class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"<Test a:{self.a} b:{self.b}>"

    def __str__(self):
        return f"From str method of Test: a is {self.a}, b is {self.b}"
t=Test(120,30)
print(repr(t))