import math

class NewtonRaphson:
    def __init__(self, function, derivative, initial_guess, precision, max_iterations):
        self.function = function
        self.derivative = derivative
        self.initial_guess = initial_guess
        self.precision = precision
        self.max_iterations = max_iterations

    def func(self, x):
        return eval(self.function.replace('x', str(x)))

    def dfunc(self, x):
        return eval(self.derivative.replace('x', str(x)))

    def calculus(self):
        x = self.initial_guess
        e = self.precision

        for i in range(self.max_iterations):
            f = self.func(x)
            df = self.dfunc(x)
            dx = -f / df
            x = x + dx
            if abs(dx) < e:
                return x

        raise ValueError("Número máximo de iterações atingido, sem solução ou aumentar as iterações")

