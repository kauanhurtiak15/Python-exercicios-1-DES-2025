# Talita está simulando o custo de frete para sua loja virtual. O valor depende da distância:

# Até 50 km: R$ 5,00
# De 51 a 150 km: R$ 15,00
# Acima de 150 km: R$ 25,00

distância = float(input("Digite a distância"))

if distância == 50:
    print("Frete de 5 reais.")
elif distância <=