# Uma empresa quer avaliar seus colaboradores com base em três metas atingidas.
# O programa deve calcular a média das três avaliações e exibir:

# Aprovado (>=7)
# Em treinamento (>=5 e <7)
# Reprovado (<5)
media1 = float(input("Digite a primeira média: "))
media2 = float(input("Digite a segunda média: "))
media3 = float(input("Digite a terceira média: "))

media = media1 or media2 or media3

print(f"media: {media:.2}")

if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Em treinamento.")
else:
    print("reprovado.")


