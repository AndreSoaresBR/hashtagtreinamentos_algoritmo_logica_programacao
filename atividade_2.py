"""
Construa um programa que calcule:
Quanto custa para encher o tanque de um carro que tem 50 litros de capacidade,
esta com 20 litros atualmente e o custo do combustivel é de R$ 5,80 por litro?
"""

capacidade_tanque = 50
volume_atual = 20
litros_encher = capacidade_tanque - volume_atual

custo_litro = 5.80
custo_total = litros_encher * custo_litro

print(f"O custo total para encher o tanque sera de R$ {custo_total}")