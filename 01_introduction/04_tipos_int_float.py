"""
Python - Tipos de Dados: int e float

Em Python, todo valor possui um tipo de dado.

Os tipos numéricos mais utilizados são:

int (integer)
    Representa números inteiros, ou seja, valores sem parte decimal.
    Exemplos: -10, 0, 25

float (floating point)
    Representa números de ponto flutuante, ou seja, valores com
    parte decimal.
    Exemplos: -3.14, 0.0, 10.5

O Python identifica automaticamente o tipo de cada valor.
Esse processo é conhecido como inferência de tipos.
"""

# ==========================================================
# Exemplo 1 - Números inteiros (int)
# ==========================================================

print(10)
print(-11)
print(0)

print()

# ==========================================================
# Exemplo 2 - Números de ponto flutuante (float)
# ==========================================================

print(1.1)
print(10.11)
print(0.0)
print(-1.5)

print()

# ==========================================================
# Exemplo 3 - Descobrindo o tipo de um valor
# ==========================================================

# A função type() retorna o tipo do objeto informado.

print(type(10))
print(type(-11))
print(type(0))

print(type(1.1))
print(type(-1.5))

print()

# ==========================================================
# Exemplo 4 - O type() funciona com outros tipos de dados
# ==========================================================

print(type("Python"))
print(type(True))

print()

# ==========================================================
# Curiosidade
# ==========================================================

# Mesmo que um número termine com ".0",
# ele continua sendo do tipo float.

print(type(10.0))
print(type(0.0))

print()

# ==========================================================
# Importante
# ==========================================================

# Em Python:
#
# 10   -> int
# 10.0 -> float
#
# Apesar de representarem o mesmo valor numérico,
# eles pertencem a tipos diferentes.

print(10 == 10.0)      # True (mesmo valor)
print(type(10))
print(type(10.0))