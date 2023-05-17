import random  # embaralhar os caracteres.
import string  # caracteres necessarios para gerar a senha.
import tkinter # criação de interface gráfica.


letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

combinacao = letras + numeros + simbolos
tamanho_senha = int(input("Qual tamanho desejado para sua senha? "))

senha = "".join(random.sample(combinacao,tamanho_senha))

print ("Sua nova senha é: " + senha)