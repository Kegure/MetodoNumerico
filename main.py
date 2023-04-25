from Bisection import Bisection
from FalsePosition import FalsePosition
from MIL import MIL
from NewtonRaphson import NewtonRaphson


def methods_options_menu():
    print("[1] Bisection Method")
    print("[2] False Position Method")
    print("[3] MIL Method")
    print("[4] NewtonRaphson")
    print("[0] Sair\n")
    option = int(input("Qual tipo de Método você deseja?\n"))
    match option:
        case 1:
            bisection = Bisection("x**3 - 9*x +3", (0, 1), 0.01, 500)
            print(bisection.calculus())
        case 2:
            falsePosition = FalsePosition("x**3 - 9*x +3", (0, 1), 0.01, 500)
            print(falsePosition.calculus())
        case 3:
            mil = MIL("x**3 - 9*x +3", (0, 1), 0.01, 500)
            print(mil.calculus())
        case 4:
            newton = NewtonRaphson("x**3 + 2*x**2 + x - 1", "3*x**2 + 4*x + 1", 0.5, 0.01, 500)
            print(newton.calculus())
        case 0:
            return print("Programa Finalizado!")
        case _:
            print("Não foi uma opção válida , tente Novamente\n")
            methods_options_menu()



methods_options_menu()

# Escrita correta de funcoes das questoes dos Slides.
# Slide 5
# Exercicio 1) x**2 + math.log(x)
# Exercicio 2) x**3 + 2*x -1
