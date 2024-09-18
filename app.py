import random 
numero_secreto = random.randint(1 , 100) #função para gerar numero aleatorio
while True: #Aqui inicio o loop até que a condição seja verdadeira (Ou seja que jogador acerte o número secreto).
    chute = int(input("Digite um número entre 1 e 100: "))#O meu INPUT vai pedir o jogador para inserir um valor inteiro(str) no console a minha função INT convertera a string para número inteiro e guarda na variavel CHUTE