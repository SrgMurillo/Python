import random

num_random = random.randint(1, 10)
print("**********************************")
print("Bem vindo ao jogo da Adivinhação!")
print("**********************************")

print("Qual nível de dificuldade?")
print("Selecione (1)Difícil (2)Médio (3)Fácil")

nivel = int(input("Definal o nivel: "))

if(nivel == 1):
    x = 10
elif nivel == 2:
    x = 15
else:
    x = 20

for tentativas in range(x):
    print("Tentativa número ", tentativas)
    chute = int(input("Informe um número entre 1 e 100: "))
    if (chute == num_random):
        print("Acertou! Você ficou com {} pontos".format(pontos_perdidos))
        break
    else:
        if (chute > num_random):
            print("Chutou um número maior!")
        else:
            print("Chutou um número menor!")
    pontos_perdidos = num_random - tentativas

print("*******************  Fim do Jogo  *******************")