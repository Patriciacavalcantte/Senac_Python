"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações.

"""
while True:
    nome_Usuario = input('Digite seu nome de usuário: ')
    senha_Usuario = input('Digite sua senha: ')

    if nome_Usuario == senha_Usuario:
        print('Senha inválida')
    else:
        print(f'Bem-vindo(a): {nome_Usuario}')
        break



