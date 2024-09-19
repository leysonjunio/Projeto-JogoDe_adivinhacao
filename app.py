import random 
numero_secreto = random.randint(1 , 100) 
while True: 
    chute = int(input("Digite um número entre 1 e 100: "))
    if chute < numero_secreto:
        print("O seu chute foi menor do que o número secreto.")
    elif chute > numero_secreto:
        print("O seu chute foi maior do que o número secreto.")
    else:
        print("Parabéns! Você acertou!")
        break