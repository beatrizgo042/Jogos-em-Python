import random
def jogar():

    print("* * * * * * * * * * * * * * * * * * * *")
    print("Olá!! Bem vindo ao jogo de adivinhação!")
    print("* * * * * * * * * * * * * * * * * * * *")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha seu nível de dificuldade")
    print("Sendo (1)Fácil, (2)Médio e (3)Difícil")
    dificuldade = int(input("Defina o nível: "))

    if(dificuldade == 1):
        total_de_tentativas = 15
    elif(dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número de 1 a 100: "))
        print("Você digitou o número ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        menor   = chute < numero_secreto
        maior   = chute > numero_secreto

        if (acertou):
            print("Parabéns, você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(menor):
                print("Você errou, o número secreto é maior.")
            elif(maior):
                print("Você errou, o número secreto é menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo.")

if(__name__ == "__main__"):
    jogar()