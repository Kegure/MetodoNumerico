class MIL:
    def __init__(self, function, intervals, precision, max_iterations):
        self.function = function
        self.intervals = intervals
        self.precision = precision
        self.max_iterations = max_iterations

    def func(self, x):
        return eval(self.function.replace('x', str(x)))

    def mil_formula(self, x, y):
        return (x*self.func(y) - y*self.func(x))/(self.func(y) - self.func(x))

    def calculus(self):
        x, y = self.intervals
        e = self.precision
        if self.func(x) * self.func(y) >= 0:
            raise ValueError("Intervalos iniciais não satisfatórios")

        for i in range(self.max_iterations):
            z = self.mil_formula(x, y)
            if abs(self.func(z)) <= e:
                return z
            if self.func(x) * self.func(z) < 0:
                y = z
            else:
                x = z
        raise ValueError("Número máximo de iterações atingido, sem solução ou aumentar as iterações")