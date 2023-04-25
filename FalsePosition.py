import math

class FalsePosition:
    def __init__(self, function, intervals, precision, max_Iterations):
        self.function = function
        self.intervals = intervals
        self.precision = precision
        self.max_Iterations = max_Iterations

    def func(self, x):
        return eval(self.function.replace('x', str(x)))

    def false_Position_Formula(self, x, y):
        return x - ((y - x) * self.func(x)) / (self.func(y) - self.func(x))

    def calculus(self):
        x, y = self.intervals
        e = self.precision

        if self.func(x) * self.func(y) <= 0:
            for i in range(self.max_Iterations):
                z = self.false_Position_Formula(x, y)
                if abs(self.func(z)) <= e:
                    return z
                if self.func(x) * self.func(z) < 0:
                    y = z
                else:
                    x = z
            raise ValueError("Numero Maximo de iterações atingida, sem solução ou aumentar o tamanho das interações")
        else:
            raise ValueError("Intervalos iniciais não satisfatórios")