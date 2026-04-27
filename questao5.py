""" 5. Essa questão você deve criar seu próprio módulo, ou seja, a questão deverá ter doisarquivos, 1 para o módulo e outro para o código principal. Imagine que você trabalhe na parte de Cyber Segurança de uma empresa e precisa testar se as senhas criadas pelos os usuários estão no padrão da empresa. O seu módulo deverá ter uma função que verifique as senhas pelos critérios:
Pelo menos 8 caracteres
Contém pelo menos uma letra maiúscula
Contém pelo menos um número
Caso os critérios não sejam seguidos informar ao usuário
Dica: utilize no seu módulo a biblioteca re """

import re
def verificar_senha(senha):
    if len(senha) < 8:
        print("A senha deve conter pelo menos 8 caracteres.")
        return False
    if not re.search(r'[A-Z]', senha):
        print("A senha deve conter pelo menos uma letra maiúscula.")
        return False
    if not re.search(r'\d', senha):
        print("A senha deve conter pelo menos um número.")
        return False
    print("Senha válida!")
    return True
def main():
    senha = input("Digite a senha para verificação: ")
    verificar_senha(senha)
main()
