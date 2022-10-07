from itertools import *
class FFF():
    def __init__(self,c:str, X:list, Y:list):
        self.X= X
        self.Y = Y
        self.c= c

    def new_list(self,X,Y,c):
        if c == "+":
            print(X.add())
        if c == "-":
            print(X.sub())
        if c == "*":
            print(X.mul())
        if c == "/":
            print(X.truediv())
    def __add__(self,other):
            return [x + y for x, y in zip_longest(X, Y, fillvalue=0)]
    def __sub__(self, other):
        return [x - y for x, y in zip_longest(X, Y, fillvalue=0)]
    def __mul__(self, other):
        X= [x * y for x, y in zip_longest(X, Y, fillvalue=0)]
        return X
    def __truediv__(self,other):
        X= [x / y for x, y in zip_longest(X, Y, fillvalue=0)]
        return X
X= FFF(list[input()])
Y= FFF(list[input()])
c= input()
print(X)

