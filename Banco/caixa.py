from conta import Conta
import os
contas = {}
sair = 0
count = 0

while sair != 1:
    os.system('cls') or None
    print("BEM VINDO AO CAIXA!")

    print("1 - Cadastrar Conta")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Extrato")
    print("5 - Verificar contas cadastradas")
    print("6 - Sair")

    resposta = int(input("Escolha uma opção acima:"))

    match resposta:
        case 1:
            titular = input("Digite o nome do titular: ")
            Conta1 = Conta(count, titular, 0.0, 1000.0)
            contas[count] = {"Titular" : Conta1.titular , "Saldo": Conta1.saldo , "Limite" : Conta1.limite} 
            count = count + 1
        case 5:
            continuar = 0
            while continuar != 1:
                for c in contas:
                    print(f"Conta de número: {c}")
                    print(contas[c])
                continuar = int(input("Se deseja voltar digite 1: "))

        case 6:
            sair = 1

print("Operações finalizadas!\nSistema Finalizando!")