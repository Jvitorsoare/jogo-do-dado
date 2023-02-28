import random

def jogar_dados():
    print("Jogando dados...")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print("Dado 1: ", dado1)
    print("Dado 2: ", dado2)
    soma = dado1 + dado2
    print("Soma: ", soma)
    if soma == 7 or soma == 11:
        print("Você ganhou!")
    elif soma == 2 or soma == 3 or soma == 12:
        print("Você perdeu!")
    else:
        print("Continue jogando!")
        ponto = soma
        while True:
            print("Jogando dados...")
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            print("Dado 1: ", dado1)
            print("Dado 2: ", dado2)
            soma = dado1 + dado2
            print("Soma: ", soma)
            if soma == ponto:
                print("Você ganhou!")
                break
            elif soma == 7:
                print("Você GANHOU!")
                break

jogar_dados()