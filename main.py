import random
import string

#Criando uma func, onde vou utilizar a biblioteca string para utilizar caracteres aleatórios
#string.ascii_letters inclui todas as letras maiúsculas e minúsculas do alfabeto.
#string.digits inclui todos os dígitos (0-9).
#string.punctuation inclui todos os caracteres de pontuação.
#Logo após utilizo a biblioteca random, utilizando a função choice()
#random.choice() --> pega os caracteres que foram fornecidos e escolhe aleatoriamente
#Juntei todos os caracteres escolhidos em uma string formando a senha
#for estou utilizando para ele escolher os caracteres até atingir o tamanho da senha desejada
def gerarSenha(tamanho = 2):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for i in range(tamanho))
    return senha
    
#Estou criando uma variavel para atribuir a função onde sera esclhido o tamanho da senha
#Logo após print do resultado da variavel
senhaGerada = gerarSenha(8)
print(f"Senha gerada: {senhaGerada}")