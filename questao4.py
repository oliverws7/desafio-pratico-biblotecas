""" 4. Vimos na nossa aula sobre Expressões Regulares (RegEx), o módulo re em Python. Sabendo disso pesquise mais sobre os recursos desse módulo e faça um programa que:
Importe re
Crie uma função extrair_telefones(texto)
Use re.findall() para encontrar números de telefone no formato: (XX) XXXXX-XXXX
Caso não encontre, informe que não encontrou
Exemplo:
Qual seu número de telefone?
Meu número é (86) 99999-1234 e (86) 99999-9876
Saída: [‘(86) 99999-12334’, ‘(86) 99999-9876’]
Retorne todos os números encontrados """

import re
def extrair_telefones(texto):
    padrao = r'\(\d{2}\) \d{5}-\d{4}'
    telefones = re.findall(padrao, texto)
    if telefones:
        print(f"Números de telefone encontrados: {telefones}")
    else:
        print("Nenhum número de telefone encontrado.")
def main():
    texto = input("Qual seu número de telefone? ")
    extrair_telefones(texto)
main()
