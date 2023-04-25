import math


def bisection_Formula(x, y):
    return (x + y) / 2


class Bisection:
    def __init__(self, function, intervals, precision, max_Iterations):
        self.function = function
        self.intervals = intervals
        self.precision = precision
        self.max_Iterations = max_Iterations

    def func(self, x):
        return eval(self.function.replace('x', str(x)))

    def calculus(self):
        x, y = self.intervals
        e = self.precision

        if self.func(x) * self.func(y) >= 0:
            raise ValueError("Intervalos iniciais não sastifatorios")

        for i in range(self.max_Iterations):
            z = bisection_Formula(x, y)
            if abs(self.func(z)) <= e:
                return z
            if self.func(x) * self.func(z) < 0:
                y = z
            else:
                x = z
        raise ValueError("Numero Maximo de iteraçoes atingida, sem solução ou aumentar as iteracoes")
