print("")

menu = """
-== Sistema Bancario Python ==-
Selecione a Opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd' or opcao == 'D':
        print("-------------")
        valor = float(input("Digite o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
        else:
            print("Valor invalido!")

    elif opcao == 's' or opcao == 'S':
        print("-------------")
        valor = float(input("Digite o valor do saque: "))

        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Excedeu seu Limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de Saques Excedidos.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor invalido!")

    elif opcao == 'e' or opcao == 'E':
        print("-------------")
        print("---Extrato---")
        print(f"Saldo: R$ {saldo:.2f}")
        print("-------------")

    elif opcao == 'q' or opcao == 'Q':
        break

    else:
        print('Operação invalida! Selecione novamente a opção desejada!')
