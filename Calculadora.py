print("Isso é uma calculadora")

n1 = float(input("Digite um numero"))

op = int(input("Escolha a operação matemática, Digite: \n 1 p/ Soma \n 2 p/ Subtração \n 3 p/ Multiplicação \n 4 p/ Divisão \n 5 p/ Potenciação"))
    
while(op < 1 or op > 5):
    print("Você não escolheu um número que represente um operador existente")
    op = int(input("Escolha a operação matemática, Digite: \n 1 p/ Soma \n 2 p/ Subtração \n 3 p/ Multiplicação \n 4 p/ Divisão \n 5 p/ Potenciação"))
    
n2 = float(input("Digite outro número"))
    
    
if op == 1:
    print(n1 + n2)
elif op == 2:
    print(n1 - n2)
elif op == 3:
    print(n1 * n2)
elif op == 4:
    if n2 == 0:
        print("Não é possível divisão por 0")
    else:
        print(n1 / n2) 
elif op == 5:
    print(n1 ** n2)



    
                 
