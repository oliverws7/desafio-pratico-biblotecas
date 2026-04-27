""" 3. Utilizando função e o módulo math crie um programa para calcular as possíveis raízes de uma equação do 2o grau. Sabendo que: ax2 + bx + c = 0. Determine e mostre o número de raízes reais distintas que a equação possui. Regra: O número de raízes reais depende do discriminante (delta), Δ = b2 - 4ac: """

import math
def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui 2 raízes reais distintas: {raiz1:.2f} e {raiz2:.2f}")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui 1 raiz real: {raiz:.2f}")
    else:
        print("A equação não possui raízes reais.")
def main():
    print("Calculadora de raízes de equação do 2º grau")
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))
    calcular_raizes(a, b, c)   
main()