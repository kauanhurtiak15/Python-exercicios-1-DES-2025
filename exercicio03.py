# Rafael trabalha com armazenamento de grãos e precisa garantir que a umidade do ar no local não ultrapasse 70%.
# Escreva um programa que receba o valor da umidade atual e exiba um alerta se estiver acima do limite.

umidade = int(input("Digite a umidade local"))

umidade = 20

if umidade >= 20:
    print("umidade normal.")
elif umidade > 20:
    print("A umidade ultrapasou o limite.")