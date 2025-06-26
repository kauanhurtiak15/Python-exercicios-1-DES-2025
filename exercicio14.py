#Loja oferece os seguintes descontos:

#Compras acima de R$ 500,00 têm 10%
#Acima de R$ 300,00 têm 5%
#Menor ou igual a R$ 300,00 não têm desconto
valor = int(input("Digite o valor da compra: "))

if valor > 500:
    print("Desconto de 10%.")
elif valor > 300:
    print("Desconto de 5%.")
elif valor <= 300:
    print("Não tem desconto.")