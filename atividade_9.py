"""
Construa um programa que calcule:
Você tem uma lista de preços de produtos, todos os produtos acima de R$ 5.000 vão ser reagustados em 5% 
e todos abaixos de R$ 5.000 vão ser reajustados em 10%, como ficam os preços dos produtos?
"""

lista_precos = [100, 6000, 1000, 5000, 1500, 5800]
reajuste_faixa1 = 0.05
reajuste_faixa2 = 0.1
corte_faixa = 5000
lista_reajustada = []

for preco in lista_precos:
    if preco >= corte_faixa:
        novo_preco = preco * (1 + reajuste_faixa1)
    else:
        novo_preco = preco * (1 + reajuste_faixa2)
    lista_reajustada.append(novo_preco)

print(f"O novo preço sera de {lista_reajustada}")