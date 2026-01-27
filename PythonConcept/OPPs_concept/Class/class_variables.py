class MyClass:
    a = 10
    b = 20               # Class variables
    def add(self):
        print(self.a + self.b)       # op: 30

mc = MyClass()
mc.add()
