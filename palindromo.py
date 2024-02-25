'''Faça um programa que leia uma string do teclado e diga se ela é palíndromo. Uma string é palíndromo quando pode ser lida tanto de trás pra frente quanto de frente para trás e possui exatamente a mesma sequência de caracteres. Considere no desenvolvimento apenas palavras palíndromos: https://www.respondeai.com.br/conteudo/strings/exercicios/faca-programa-leia-string-teclado-diga-palindromo-string-palindromo-pode-10903'''
#Desenvolvido por Ulisses F. Falcão em 16/02/2024

import pypalindromo

msnEntrada = 'Digite o que quiser:\n'
msnTrue = '{} é \"PALÍNDROMO\"'
msnFalse = 'Não é palíndromo!'
entrada = input(msnEntrada)

if pypalindromo.palindromo(entrada) == True:
    print(msnTrue.format(entrada))
else:
    print(msnFalse)