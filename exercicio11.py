#crie um programa que receba o peso (kg) e a altura (m) de uma pessoa e calcule o IMC.
#classifique o resultado de acordo com a faixa:

#Abaixo do peso(< 18.5)
#Peso normal(18.5 a 24.9)
#Sobrepeso(25 a 29.9)
#Obesidade(>=30)

peso = float(input("Digite o peso da pessoa: "))
altura = float(input("Digite a altura da pessoa: "))

IMC = peso/altura
if peso < 18.5:
    print("Abaixo do peso.")
elif peso <= 18.5 >= 24.9:
    print("Peso normal.")
else:
    print("sobrepeso.")