import random

def jogar():
    print("***********************")
    print("***Bem vindo a forca***")
    print("***********************")

    arquivo = open("lista.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0,len(palavras))
    palavra = palavras[numero].upper()
    letra_acertada = ["_" for letra in palavra]
    erros = 0
    enforcou = False
    acertou = False

    print(letra_acertada)

    while(not enforcou and not acertou):
        print("jogando...")
        chute = input("Qual letra??? ")
        chute = chute.strip().upper()
        if(chute in palavra):     
            index = 0
            for letra in palavra: 
                if(chute == letra):
                    letra_acertada[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == 6    
        acertou = "_" not in letra_acertada 
        print(letra_acertada)
    if(acertou):
        print("Parabens, você ganhou")  
    else:
        print("Voce perdeu :(")
        print(palavra)
    print("Fim de Jogo")
if(__name__ == "__main__"):
    jogar()