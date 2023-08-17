class demo:
    a=10
    b=20
    c = a+b

    def add(self):
        x=20
        y = 20
        z = x+y
        return z

    def show(self):
        print("hello")
obj = demo()
r = obj.c
print(r)
obj1 = demo()
z = obj1.add()
print(z)

obj2 = demo()
obj2.show()


class A:
    def disA(self):
        print("Display A")

class B(A):
    def disB(self):
        print("Display B")

class C(B):
    def disC(self):
        print("Display C")

obj = C()
obj.disA()
obj.disB()
obj.disC()
