idade = int(input("Digite a idade para verificar: "))

if idade >= 16 and idade <= 17:
    print("Eleitor facultativo!")
elif idade >= 18 and idade <= 65:
    print("Eleitor obrigatório!")
elif idade > 65:
    print("Dispensado!")
else:
    print("Ainda não pode votar! Aguarde a idade!")
