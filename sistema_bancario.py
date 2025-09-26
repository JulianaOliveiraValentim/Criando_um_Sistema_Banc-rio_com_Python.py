# Criando um Sistema Bancário com Python
'''
Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. 
O objetivo é implementar três operações essenciais: depósito, saque e extrato. 
-> depósito: adicionar dinheiro à conta
-> saque: retirar dinheiro da conta
    --> cada saque tem o limite de 500 reais
    --> o saldo da conta não pode ser negativo
    --> limitado a 3 saques por dia
-> extrato: mostrar o saldo da conta
    --> mostra os saques e depósitos realizados,em ordem cronológica
'''

# Sistema Bancário em Python

# Variáveis iniciais
saldo = 0
limite_saque = 500
saques_realizados = 0
limite_saques = 3
extrato = []

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("O valor do depósito deve ser positivo.")

def sacar(valor):
    global saldo, saques_realizados
    if saques_realizados >= limite_saques:
        print("Limite de saques diários atingido!")
        return
    if valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite_saque:
        print(f"O valor do saque excede o limite de R$ {limite_saque:.2f}")
    elif valor <= 0:
        print("O valor do saque deve ser positivo.")
    else:
        saldo -= valor
        saques_realizados += 1
        extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def mostrar_extrato():
    print("\n=== EXTRATO ===")
    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("================\n")

# Loop principal
while True:
    print("Escolha uma operação:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: R$ "))
        depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: R$ "))
        sacar(valor)
    elif opcao == "3":
        mostrar_extrato()
    elif opcao == "4":
        print("Obrigado por usar o sistema bancário!")
        break
    else:
        print("Opção inválida. Tente novamente.")