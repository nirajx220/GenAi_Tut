class A:
    label  = "A Base class"


class B(A):
    label = "B:   mashala blend"


class C(A):
    label = "C:   Harbal blend"

class D(B, C):
    # label = "D:   Special blend"    
    pass


cup = D()
print(cup.label)
print(D.__mro__)