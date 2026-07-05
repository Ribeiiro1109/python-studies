"""
Python - Entrada de Dados com input()

A função input() permite receber dados digitados pelo usuário durante
a execução do programa.

Importante:
Todo valor retornado por input() é do tipo string (str). Quando for
necessário realizar operações matemáticas, o valor deve ser convertido
para um tipo numérico, como int ou float.
"""

# ==========================================================
# Recebendo informações do usuário
# ==========================================================

nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")

print(f"Seu nome é {nome} e sua idade é {idade}.")

print()

# ==========================================================
# Convertendo valores para realizar uma soma
# ==========================================================

numero1 = input("Digite um número: ")
numero2 = input("Digite outro número: ")

# input() retorna uma string. Por isso, é necessário converter
# os valores para int antes de realizar a soma.
int_numero1 = int(numero1)
int_numero2 = int(numero2)

soma = int_numero1 + int_numero2

print(f"Soma: {soma}")