a = int(input("DIgite o valor de A: "))
b = int(input("DIgite o valor de B: "))

if a > b:
    aux = a
    a = b
    b = aux

print(f"Em ordem crescente: {b, a}")
