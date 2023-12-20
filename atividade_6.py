"""
Construa um programa que calcule:
Qual seria o salario de um funcionario apos 10 anos se todo ano ele ganhasse 10% de aumento,
com um salario inicial de R$ 2.000?
"""

salario = 2000
aumento = 0.1
tempo = 10

for ano in range (tempo):
    salario = salario * (1 + aumento)

print(f"Seu salario final sera de R$ {salario}")