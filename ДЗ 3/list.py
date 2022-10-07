from itertools import *
class FFF():
    def __init__(self, X, Y, c):
        self.X= X
        self.Y = Y
        self.c= c

    def new_list(self):
        if c == "+":
            print(X.add())
        if c == "-":
            print(X.sub())
        if c == "*":
            print(X.mul())
        if c == "/":
            print(X.truediv())
    class HHH():
        def add(self,other):
                return [x + y for x, y in zip_longest(X, Y, fillvalue=0)]
        def sub(self, other):
            return [x - y for x, y in zip_longest(X, Y, fillvalue=0)]
        def mul(self, other):
            return [x * y for x, y in zip_longest(X, Y, fillvalue=0)]
        def truediv(self,other):
            return [x / y for x, y in zip_longest(X, Y, fillvalue=0)]
X= FFF((list(input())))
Y= FFF(list(input()))
c= FFF(list(input()))
X,Y,c.new_list()

