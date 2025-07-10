valor=5
valor01=5

print(f"a soma é {valor *2}")

idade = (input("Digite sua idade: "))
nota = float(input("Digite sua nota: "))
print("Está na faixa etária especial?", idade > 10 and idade < 18)
print("Nota extrema?", nota < 5 or nota > 9)

idade = int(input("Digite a idade: "))
if idade > 18:
    print("Maior de idade")
