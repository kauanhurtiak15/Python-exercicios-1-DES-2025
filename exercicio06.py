# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.
plataforma = int(input("Digite que horas você quer acessar a plataforma: "))

if plataforma < 9:
    print("Acesso negado.")
elif plataforma > 9:
    print("Acesso permitido.")
