print("🛒 Loja Python – Compras do Dia!")

p1 = float(input("Produto 1 - preço: R$ "))
q1 = int(input("Quantidade: "))

p2 = float(input("Produto 2 - preço: R$ "))
q2 = int(input("Quantidade: "))

p3 = float(input("Produto 3 - preço: R$ "))
q3 = int(input("Quantidade: "))

total = (p1*q1) + (p2*q2) + (p3*q3)
desconto = total * 0.10
final = total - desconto

print(f"\nTotal bruto: R$ {total:.2f}")
print(f"Desconto (10%): R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {final:.2f}")
