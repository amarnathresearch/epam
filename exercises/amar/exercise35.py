class Calc:
    def add(self, x, y):
        return x+y

    def sub(self, x, y):
        return x-y

    def mul(self, x, y):
        return x*y

    def div(self, x, y):
        if x == 0 or y == 0:
            return -1
        return x/y