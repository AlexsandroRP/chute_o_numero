from random import randint

def gerar_numero():
    numero = randint(1,100)
    return numero

numero_aleatorio = gerar_numero()
print("foi gerado um número entre 1 e 100...")

continuar_game = True

while continuar_game:
    chute = int(input("Chute um número de 1 a 100: "))
    if chute == numero_aleatorio:
        print(f"PARABÉNS! VOCÊ CHUTOU O VALOR CERTO: {chute}")
        continuar_encerrar = input("Jogo encerrado, gostaria de jogar novamente?(s/n) ").lower()
        if continuar_encerrar == 'n':
            print("-"*30)
            print("Encerrando o jogo...")
            print("-"*30)
            continuar_game = False
        else:
            continuar_game = True
            numero_aleatorio = gerar_numero()    
    elif chute < numero_aleatorio:
        print("Chute um número maior")
    else:
        print("Chute um número menor")    
#input("Pressione ENTER para iniciar...")