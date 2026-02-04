a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

if a <= b and a <= c:
    menor = a
    if b <= c:
        medio = b
        maior = c
    else:
        medio = c
        maior = b
        
elif b <= a and b <= c:
    menor = b
    if a <= c:
        medio = a
        maior = c
    else:
        medio = c
        maior = a
else:
    menor = c
    if a <= b:
        medio = a
        maior = b
    else:
        medio = b
        maior = a

print(f"Os números em ordem crescente é: {menor} {medio} {maior}")
