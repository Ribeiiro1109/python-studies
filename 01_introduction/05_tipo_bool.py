"""
Python - Tipo de Dado bool (Boolean)

O tipo bool representa valores lógicos e possui apenas dois
resultados possíveis:

True  -> Verdadeiro
False -> Falso

Valores booleanos são amplamente utilizados em comparações,
estruturas condicionais (if, elif e else) e operadores lógicos.
"""

# ==========================================================
# Exemplo 1 - Comparando valores
# ==========================================================

# O operador de igualdade (==) verifica se dois valores
# são iguais.

print(10 == 10)   # True
print(10 == 11)   # False

print()

# ==========================================================
# Exemplo 2 - Armazenando o resultado de uma comparação
# ==========================================================

# O resultado de uma comparação pode ser armazenado
# em uma variável.

resultado = 20 > 10

print(resultado)

print()

# ==========================================================
# Exemplo 3 - Descobrindo o tipo de um valor
# ==========================================================

# A função type() retorna o tipo do objeto informado.

print(type(True))
print(type(False))
print(type(10 == 10))

print()

# ==========================================================
# Exemplo 4 - Outras comparações
# ==========================================================

print(5 > 2)       # True
print(5 < 2)       # False
print(8 >= 8)      # True
print(10 != 10)    # False

print()

# ==========================================================
# Curiosidade
# ==========================================================

# O resultado de qualquer comparação em Python
# será sempre um valor booleano (True ou False).

print(type(100 > 50))
print(type("Python" == "Python"))

print()

# ==========================================================
# Importante
# ==========================================================

# Apesar de serem exibidos como palavras,
# True e False não são strings.
#
# Eles pertencem ao tipo bool.

print(type(True))
print(type(False))