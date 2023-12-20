"""
Construa um programa que calcule:
Qual deve ser o bonus de um funcionario? Se ele vendeu mais de 1.000 unidades,
o bonus é de R$ 250,00 se não, o bonus é de R$ 50,00.
"""

meta = 1000
vendas = 800

if vendas > meta:
    bonus = 250
else:
    bonus = 50

print(f"O valor do seu bonus sera de R$ {bonus}")