# Renata quer solicitar um financiamento, mas precisa verificar se cumpre os critérios:

# Salário mensal acima de R$ 3.000,00
# A parcela não pode ser maior que 35% do salário
saláriomensal = float(input("Digite o saláriomensal"))
parcela = float(input("Digite a parcela"))

if saláriomensal >= 3000 and parcela <= 35:
    print("Seu financiamento foi solicitado.")
else:
    print("Os critérios não foram atendidos.")