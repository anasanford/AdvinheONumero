import random

def advinhe(x):
    numero_aleatorio = random.randint(1, x)
    chute = 0
    while chute != numero_aleatorio:
        chute = int(input(f"Chute um número entre 1 e {x}: "))
        if chute < numero_aleatorio:
            print('Que pena! Tente novamente. Número muito baixo.')
        elif chute > numero_aleatorio:
            print('Que pena! Tente novamente. Número muito alto.')
    print('Parabéns! Você advinhou o número!')

def computador_advinha(x):
    menor = 1
    maior = x
    feedback = ''
    while feedback != 'c':
        if menor != maior:
            chute = random.randint(menor, maior)
        else:
            chute = menor   # poderia ser maior também, pois menor = maior nesse caso.
        feedback = input(f"O chute {chute} está muito alto(A), muito baixo (B) ou correto(C)?: ").lower()
        if feedback == 'a':
            maior = chute - 1
        elif feedback == 'b':
            menor = chute + 1
    print("Eba! O computador advinhou o seu número!")

print('Bem vindo(a) ao jogo Advinhe o Número! \nTente advinhar o número secreto do computador.')
advinhe(1000)

print("----------------------------------------------")
print("Agora é a sua vez de escolher um número secrete entre 1 e 1000 para o computador advinhar! \n" \
"Escolha um número e dê ao computador um feedback sobre o chute dele.")
computador_advinha(1000)
print("Obrigada por jogar!")
