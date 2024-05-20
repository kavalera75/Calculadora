print("Isso é uma calculadora")

n1 = float(input("Digite um numero"))

op = int(input("Escolha a operação matemática, Digite: \n 1 p/ Soma \n 2 p/ Subtração \n 3 p/ Multiplicação \n 4 p/ Divisão \n 5 p/ Potenciação"))

n2 = float(input("Digite outro número"))


operacoes = {
    1: print(n1 + n2),
    2: print(n1 - n2),
    3: print(n1 * n2),
    4: print(n1 / n2),
    5: print(n1 ** n2)
}

resultado = operacoes.get(op, "Operação inválida")(n1, n2)
print("Resultado: ", resultado)