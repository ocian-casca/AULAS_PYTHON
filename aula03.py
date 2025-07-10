print(" Calculadora Python")
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = input("Digite o número da operação desejada: ")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if op == "1":
    resultado = n1 + n2
    print(f"Resultado da soma: {resultado}")
elif op == "2":
    resultado = n1 - n2
    print(f"Resultado da subtração: {resultado}")
elif op == "3":
    resultado = n1 * n2
    print(f"Resultado da multiplicação: {resultado}")
elif op == "4":
    resultado = n1 / n2
    print(f"Resultado da divisão: {resultado}")
else:
    print("Operação inválida.")
