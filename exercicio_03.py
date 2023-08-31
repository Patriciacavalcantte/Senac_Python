"""

3.	Faça um programa que leia e valide as seguintes informações:
a.	Nome: maior que 3 caracteres;
b.	Idade: entre 0 e 150;
c.	Salário: maior que zero;
d.	Sexo: 'f' ou 'm';
e.	Estado Civil: 's', 'c', 'v', 'd';


"""
nome = 'Patrícia Cavalcante'
idade = 37
salario = 26.196
sexo = 'f'
estado_civil = 'c'

if len(nome) >= 3:
     print(f'Seu nome é {nome}, que é válido.')
if idade >= 0 and idade <= 150:
     print(f'Sua idade é {idade}, e é válida.')

if salario >0:
     print(f'Seu salário é {salario}, e é válido.')

if sexo in ['s', 'c', 'v', 'd']:
     print(f'Seu sexo é {sexo}, e é válido.')

if estado_civil in ['s', 'c', 'v', 'd']:
     print(f'Seu estado civil é {estado_civil}, que é válido.')
else:
     print('Dados inválidos!')