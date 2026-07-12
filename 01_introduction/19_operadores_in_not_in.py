"""
Python - Operadores IN e NOT IN

Os operadores `in` e `not in` são utilizados para verificar
se um valor está presente em uma sequência.

Esses operadores podem ser utilizados com diversos tipos de dados,
como strings, listas, tuplas e dicionários.

Neste exemplo, utilizaremos strings.

Strings são sequências de caracteres (iteráveis), ou seja,
cada caractere possui uma posição (índice).

Índices positivos:

  0  1  2  3  4  5  6
  R  i  b  e  i  r  o

Índices negativos:

 -7 -6 -5 -4 -3 -2 -1
  R  i  b  e  i  r  o
"""

# ==========================================================
# Exemplo 1 - Acessando caracteres de uma string
# ==========================================================

nome = "Ribeiro"

# Índices positivos começam em 0.
print(nome[2])   # b

# Índices negativos começam em -1 (último caractere).
print(nome[-7])  # R

print()

# ==========================================================
# Exemplo 2 - Operador IN
# ==========================================================

# O operador "in" verifica se um valor existe na sequência.

print("i" in nome)
print("a" in nome)
print("iro" in nome)

print()

# ==========================================================
# Exemplo 3 - Operador NOT IN
# ==========================================================

# O operador "not in" verifica se um valor NÃO existe
# na sequência.

print("b" not in nome)
print("d" not in nome)

print()

# ==========================================================
# Importante
# ==========================================================

# Os operadores "in" e "not in" diferenciam letras
# maiúsculas de minúsculas.

print("R" in nome)   # True
print("r" in nome)   # True
print("B" in nome)   # False

# Isso acontece porque "B" e "b" são caracteres diferentes.