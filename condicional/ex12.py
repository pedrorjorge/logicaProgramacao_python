p = int(input("Digite a posição da bola P (0 ou 1): "))
r = int(input("Digite a posição da bola R (0 ou 1): "))

if p == 0 and r == 0:
    caminho = "A"
elif p == 0 and r == 1:
    caminho = "B"
elif p == 1 and r == 0:
    caminho = "B"
elif p == 1 and r == 1:
    caminho = "C"
else:
    print("Caminho inválido!")

print(f"A bolinha seguirá pelo caminho: {caminho}")
