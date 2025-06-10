# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.
consumo = int(input("Digite quanto foi o consumo mensal:"))

if consumo < 100:
    print("Consumo dentro do limite.")
elif consumo > 100:
    print("Consumo ultrapassou o limite.")
