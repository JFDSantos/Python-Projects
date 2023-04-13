from conta import Conta
import os
import time
sair = 0

ContaAtual = []

while sair != 1:
    os.system('cls') or None
    print("BEM VINDO AO CAIXA!")

    print("\n1 - Entrar na Conta")
    print("2 - Sair")

    try:
        resposta = int(input("\nEscolha uma opção acima: "))
    except:
        resposta = 2

    match resposta:
        case 1:
            resposta = 0
            titular = input("\nDigite o nome do titular: ")
            numero = input("Digite o número da sua conta: ")
            Conta1 = Conta(numero, titular, 0.0, 1000.0)
            os.system('cls') or None
            while sair != 1:
                print("\nFUNCIONALIDADES: ")
                print("1 - Sacar")
                print("2 - Depositar")
                print("3 - Extrato")
                print("4 - Sair")

                resposta =  int(input("\nEscolha uma opção acima: "))

            
                match resposta:
                    case 1:
                        valor = int(input("\nDigite o valor que deseja sacar: R$"))
                        if valor < Conta1.saldo:
                            Conta1.sacar(valor)
                            print("\nSaque realizado!")
                        else:
                            print("\nDinheiro insuficiente")
                        
                        time.sleep(3)
                    case 2:
                        valor = int(input("\nDigite o valor que deseja depositar: R$"))
                        Conta1.depositar(valor)
                        print("\nValor depositado!")
                        time.sleep(3)
                    case 3:
                        voltar = 0

                        while voltar != 1:
                            print(f"Titular: {Conta1.titular}")
                            print(f"Conta:   {Conta1.numero}")
                            print(f"Saldo:   R${Conta1.saldo}")
                            voltar = int(input("\nPara voltar digite 1: "))
                    case 4:
                        sair = 1
        case 2:
            sair = 1

print("\nOperações finalizadas!\tSistema Finalizando!")