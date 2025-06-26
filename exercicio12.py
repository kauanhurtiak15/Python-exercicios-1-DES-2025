#Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
#Exiba uma mensagem de "Senha válida" ou "Senha muito curta".
senha = int(input("digite uma senha: "))

if senha >= 8:
    print("Senha válida.")
else:
    print("Senha muito curta.")
