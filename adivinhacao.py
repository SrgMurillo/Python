import random

num_random = random.randint(1, 20)
print("**********************************")
print("Bem vindo ao jogo da Adivinhação!")
print("**********************************")

passe = 1
while(passe==1):
    chute = int(input("Informe um número entre 1 e 20: "))
    if (chute == num_random):
        print("Acertou!")
        break
    else:
        if (chute > num_random):
            print("Chutou um número maior!")
        else:
            print("Chutou um número menor!")
    passe = int(input("Informe 0 para deixar o programa e 1 para tentar novamente!\n"))
