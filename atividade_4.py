"""
Construa um programa que calcule:
Qual deve ser o bonus de um funcionario? Se a empresa bateu a meta de 10.000 vendas e se ele vendeu mais de 1.000 unidades,
o bonus tem que ser de R$ 250,00 se não, o bonus tem que ser de R$ 50,00.
"""

vendas = 10000
meta = 1000

vendas_empresa = 10500
meta_funcionario = 1300

if vendas_empresa >= vendas and meta_funcionario >= meta:
    bonus = 250
else:
    bonus = 50

print(f"O valor do seu bonus sera de R$ {bonus}")