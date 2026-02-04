t1 = int(input("Digite a quantidade de tomadas para a regua 1:"))
t2 = int(input("Digite a quantidade de tomadas para a regua 2:"))
t3 = int(input("Digite a quantidade de tomadas para a regua 3:"))
t4 = int(input("Digite a quantidade de tomadas para a regua 4:"))

quantidadeTomadas = (t1+t2+t3+t4) - 3

print(f"A quantidade de notebooks que poderão ser ligados é: {quantidadeTomadas}")
