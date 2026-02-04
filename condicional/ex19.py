valorCompra = float(input("Digite o valor da sua compra: "))

if valorCompra <= 100.00:
    desconto = 0.05
elif valorCompra > 100.00 and valorCompra < 200.00:
    desconto = 0.10
elif valorCompra > 200.00:
    desconto = 0.20

valorDesconto = valorCompra * desconto
novoValor = valorCompra - valorDesconto

print(f"O valor do desconto é: {valorDesconto}")
print(f"O valor total com o desconto aplicado é: {novoValor}")
