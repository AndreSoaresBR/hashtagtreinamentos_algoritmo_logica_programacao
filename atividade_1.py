"""
Construa um programa que calcule:
Quanto devemos cobrar em um projeto de programação se trabalharmos 8 horas por dia,
demorando 15 dias para fazer o projeto e cobramos R$ 100,00 a hora?
"""

horas_por_dia = 8
dias_trabalhado = 15
horas_trabalho = horas_por_dia * dias_trabalhado

custo_hora = 100
custo_do_tabalho = horas_trabalho * custo_hora

print(f"O valor total a ser cobrado sera de R$ {custo_do_tabalho}")