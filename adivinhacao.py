import random

num_random = random.randint(1, 20)
print("**********************************")
print("Bem vindo ao jogo da Adivinhação!")
print("**********************************")

chute = int(input("Informe um número entre 1 e 20: "))

if (chute == num_random):
    print("Acertou!")
else:
    if (chute > num_random):
        print("Chutou um número maior!")
    else:
        print("Chutou um número menor!")
