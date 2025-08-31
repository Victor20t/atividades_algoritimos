kg_maca = float(input("Quantos Kg de maçã? "))
kg_morango = float(input("Quantos Kg de morango? "))

if kg_maca > 5:
    preco_maca = kg_maca * 1.50
else:
    preco_maca = kg_maca * 1.80

if kg_morango > 5:
    preco_morango = kg_morango * 2.20
else:
    preco_morango = kg_morango * 2.50

preco_total = preco_maca + preco_morango
kg_total = kg_maca + kg_morango

if kg_total > 8 or preco_total > 25:
    desconto = preco_total * 0.10
    preco_final = preco_total - desconto
else:
    preco_final = preco_total

print(f"Você comprou {kg_maca} KG de maçã que deu R$ {preco_maca:.2f}")
print(f"Você comprou {kg_morango} KG de morango que deu R$ {preco_morango:.2f}")
print(f"Total de {kg_total} KG e R$ {preco_final:.2f}")
