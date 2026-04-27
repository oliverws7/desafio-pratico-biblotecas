""" 1. Jogo de Adivinhação. Utilizando a biblioteca random crie um pequeno jogo de adivinhação de números inteiros que deve ir de 1 a 100. As regras do jogo devem ser:
Todos os palpites do usuário devem ser armazenados
O programa deve informar que o usuário errou o palpite e mostrar uma dica se o número a ser descoberto é maior ou menor do que o número do palpite
Quando o usuário acertar o palpite o programa deve mostrar: todos os números digitados para o palpite, a quantidade de tentativa """

import random
def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    palpites = []
    while True:
        palpite = int(input("Digite um número entre 1 e 100: "))
        palpites.append(palpite)
        if palpite < numero_secreto:
            print("Errou! O número é maior.")
        elif palpite > numero_secreto:
            print("Errou! O número é menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto}.")
            print(f"Palpites: {palpites}")
            print(f"Quantidade de tentativas: {len(palpites)}")
            break
jogo_adivinhacao()
