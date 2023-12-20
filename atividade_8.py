"""
Construa um programa que calcule:
Tenho uma lista de preços de produtos, se fizermos um reajuste de 5% a mais em todos os produtos,
como ficam os preços dos produtos?
"""

lista_preco = [100, 500, 1000, 1500]
reajuste = 0.05
lista_reajustada = []

for preco in lista_preco:
    novo_preco = preco * (1 + reajuste)
    lista_reajustada.append(novo_preco)

print(f"O novo preço sera de {lista_reajustada}")