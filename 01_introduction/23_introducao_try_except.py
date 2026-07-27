"""
Python - Introdução ao try/except

O tratamento de exceções permite que um programa lide com erros
de forma controlada, evitando que ele seja encerrado inesperadamente.

Estrutura básica:

try:
    # Código que pode gerar um erro.
except:
    # Código executado caso ocorra um erro.

Neste exemplo, o usuário deve informar um número para que
o programa calcule o seu dobro.
"""

# ==========================================================
# Exemplo 1 - Validando a entrada com isdigit()
# ==========================================================

numero = input("Digite um número para calcular o dobro: ")

# O método isdigit() verifica se a string contém apenas dígitos.
# Caso contrário, evita que o programa tente realizar uma conversão inválida.
if numero.isdigit():
    numero_float = float(numero)
    print(f"O dobro de {numero} é {numero_float * 2}")
else:
    print("Você não digitou um número válido.")

print()

# ==========================================================
# Exemplo 2 - Tratando erros com try/except
# ==========================================================

# O bloco try tenta executar o código.
# Caso ocorra algum erro, o bloco except será executado.

try:
    numero_float = float(numero)
    print(f"O dobro de {numero} é {numero_float * 2}")

except:
    print("Você não digitou um número válido.")

print()

# ==========================================================
# Curiosidade
# ==========================================================

# O método isdigit() funciona apenas para números inteiros positivos.
#
# Exemplos:
#
# "10"    -> True
# "-10"   -> False
# "10.5"  -> False
# "abc"   -> False

print("10".isdigit())
print("-10".isdigit())
print("10.5".isdigit())
print("abc".isdigit())

print()

# ==========================================================
# Importante
# ==========================================================

# Nesta aula foi utilizado apenas "except:" para simplificar.
#
# Em programas reais, é recomendado capturar exceções
# específicas, por exemplo:
#
# except ValueError:
#
# Esse assunto normalmente é estudado mais adiante no curso.