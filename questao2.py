""" 2. O professor de matemática Alan Turing pediu sua ajuda para criar um pequeno sistemapara calcular as áreas das figuras planas. Ele pediu que o usuário possa escolher qual figura quer calcular. Para cada cálculo de uma figura faça uma função específica. Utilize a figura abaixo como apoio matemático e das figuras que seu programa deve conter. """

import math
def area_circulo():
    raio = float(input("Digite o raio do círculo: "))
    area = math.pi * (raio ** 2)
    print(f"A área do círculo é: {area:.2f}")
def area_triangulo():
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area:.2f}")
def area_retangulo():
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area = largura * altura
    print(f"A área do retângulo é: {area:.2f}")
def area_quadrado():
    lado = float(input("Digite o lado do quadrado: "))
    area = lado ** 2
    print(f"A área do quadrado é: {area:.2f}")
def area_trapezio():
    base_maior = float(input("Digite a base maior do trapézio: "))
    base_menor = float(input("Digite a base menor do trapézio: "))
    altura = float(input("Digite a altura do trapézio: "))
    area = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é: {area:.2f}")
def area_losango():
    diagonal_maior = float(input("Digite a diagonal maior do losango: "))
    diagonal_menor = float(input("Digite a diagonal menor do losango: "))
    area = (diagonal_maior * diagonal_menor) / 2
    print(f"A área do losango é: {area:.2f}")
def main():
    while True:
        print("\nEscolha a figura para calcular a área:")
        print("1. Círculo")
        print("2. Triângulo")
        print("3. Retângulo")
        print("4. Quadrado")
        print("5. Trapézio")
        print("6. Losango")
        print("7. Sair")
        escolha = input("Digite o número da figura: ")
        if escolha == '1':
            area_circulo()
        elif escolha == '2':
            area_triangulo()
        elif escolha == '3':
            area_retangulo()
        elif escolha == '4':
            area_quadrado()
        elif escolha == '5':
            area_trapezio()
        elif escolha == '6':
            area_losango()
        elif escolha == '7':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()
