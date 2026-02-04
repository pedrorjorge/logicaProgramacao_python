a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))
c = int(input("Digite o valor de C:"))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Não existe raiz real")
elif delta == 0:
    print("Existe raiz real")
elif delta > 0:
    print("Existe 2 raizes reais diferentes")
    
