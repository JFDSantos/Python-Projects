import random

print("\nPROJETO FORCA\n")

listaDePalavras = open("forca\palavras.txt", 'r')
palavras = []

for linha in listaDePalavras:
        linha = linha.strip()
        palavras.append(linha)

listaDePalavras.close()

numero = random.randrange(0, len(palavras))
palavra = palavras[numero].upper()


palavraTentada = ["-" for letra in palavra]
acertou = False
enforcou = False
tentativa = 7

while (not acertou and not enforcou):
    print("\nTentativas Restantes: ", tentativa)
    letra = input("Digite uma letra: ").upper()

    if letra in palavra:
        index = 0 
        for l in palavra:
            if letra == l:
                palavraTentada[index] = letra
            index = index + 1
    else:
        tentativa = tentativa - 1

    print(f"\n{''.join(palavraTentada)}")
    enforcou = tentativa == 0
    acertou = '-' not in palavraTentada

if acertou:
    print(f"\nParabens, voce venceu!! A palavra era {palavra}")
else:
    print(f"\nVoce perdeu!! A palavra era {palavra}")