"""
Construa um programa que calcule:
Calcule o contrario agora, quanto tempo demora para esse funcionario chegar em um salario de R$ 10.000?
"""

salario = 2000
aumento = 0.1
tempo = 0

while salario < 10000:
    salario = salario * (1 + aumento)
    tempo = tempo + 1

print(f"Levera {tempo} anos para chegar no salario de R$ 10.000,00")