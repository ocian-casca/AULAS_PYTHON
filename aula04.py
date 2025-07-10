print("🏦 Bem-vindo ao Caixa Eletrônico Python")

# Saldo inicial fictício
saldo = 1000.00

print("\nEscolha uma operação:")
print("1 - Consultar saldo")
print("2 - Sacar")
print("3 - Depositar")
print("4 - Sair")

op = input("Digite a opção desejada: ")

if op == "1":
    print(f"💰 Seu saldo atual é: R$ {saldo:.2f}")
elif op == "2":
    saque = float(input("Digite o valor para sacar: "))
    if saque <= saldo:
        saldo = saldo - saque
        print(f"✅ Saque realizado! Novo saldo: R$ {saldo:.2f}")
    else:
        print("❌ Saldo insuficiente!")
elif op == "3":
    deposito = float(input("Digite o valor para depositar: "))
    saldo = saldo + deposito
    print(f"✅ Depósito realizado! Novo saldo: R$ {saldo:.2f}")
elif op == "4":
    print("👋 Saindo... obrigado por usar nosso banco!")
else:
    print("❌ Opção inválida!")
