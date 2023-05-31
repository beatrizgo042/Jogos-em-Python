import forca
import adivinhacao

def escolhe_jogo():
    print("* * * * * * * * * * * * * *")
    print("* * Escolha o seu jogo! * *")
    print("* * * * * * * * * * * * * *")

    print("(1) Forca - (2) Adivinhação.")

    escolha = int(input("Digite qual jogo: "))

    if(escolha == 1):
        print("Jogando o jogo da forca...")
        forca.jogar()
    elif(escolha == 2):
        print("Jogando o jogo de adivinhação...")
        adivinhacao.jogar()


if(__name__ == "__main__"):
    escolhe_jogo()