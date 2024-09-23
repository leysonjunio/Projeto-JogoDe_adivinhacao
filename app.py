import random 
from tkinter import*
def jogo():
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
janela = tk() #Criar a janela principal 
janela.title("Adivinhe o Número")

rotulo = Label(janela, text="Adivinhe um número entre 1 e 100:")
rotulo.pack()#Rótulo com instruções



janela.mainloop()