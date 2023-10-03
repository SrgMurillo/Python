import random

num_random = random.randint(1, 20)
print("**********************************")
print("Bem vindo ao jogo da Adivinhação!")
print("**********************************")

tentativas = 1
while(tentativas <= 3):
    print("Tentativa número ", tentativas)
    chute = int(input("Informe um número entre 1 e 20: "))
    if (chute == num_random):
        print("Acertou!")
        break
    else:
        if (chute > num_random):
            print("Chutou um número maior!")
        else:
            print("Chutou um número menor!")

    tentativas += 1

print("*******************  Fim do Jogo  *******************")