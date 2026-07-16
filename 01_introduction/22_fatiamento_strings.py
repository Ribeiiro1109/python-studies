"""
Python - Fatiamento de Strings (String Slicing)

O fatiamento permite acessar apenas uma parte de uma string.

Sintaxe:

string[inicio:fim:passo]

Onde:

inicio -> Índice inicial (inclusivo)
fim    -> Índice final (não inclusivo)
passo  -> Define de quantas em quantas posições a string será percorrida

Se algum parâmetro for omitido, o Python utilizará um valor padrão.

Exemplos:

[:5]   -> Do início até a posição 5 (não inclusiva)
[3:]   -> Da posição 3 até o final
[::2]  -> Percorre de 2 em 2 caracteres
[::-1] -> Inverte a string

A função len() retorna a quantidade de caracteres da string.
"""

# ==========================================================
# Exemplo 1 - Índices positivos
# ==========================================================

texto = "Olá mundo"

# Índices positivos:
#
#  012345678
#  Olá mundo

print(texto[:3])   # Olá
print(texto[3:])   #  mundo

print(f"Quantidade de caracteres: {len(texto)}")

print()

# ==========================================================
# Exemplo 2 - Índices negativos
# ==========================================================

nome = "João Victor"

# Índices negativos:
#
# -11........-1
# João Victor

print(nome[-11:-6])   # João
print(nome[-6:])      # Victor

print(f"Quantidade de caracteres: {len(nome)}")

print()

# ==========================================================
# Exemplo 3 - Utilizando o passo (step)
# ==========================================================

palavra = "Programador"

# Percorre a string de duas em duas posições.
print(palavra[::2])

# Percorre a string de trás para frente,
# pulando duas posições por vez.
print(palavra[::-2])

print(f"Quantidade de caracteres: {len(palavra)}")

print()

# ==========================================================
# Exemplo 4 - Invertendo uma string
# ==========================================================

print(palavra[::-1])

print()

# ==========================================================
# Exemplo 5 - Fatiamento informado pelo usuário
# ==========================================================

texto = input("Digite uma palavra: ")

print(f"Primeiros 3 caracteres: {texto[:3]}")
print(f"Últimos 3 caracteres: {texto[-3:]}")
print(f"Texto invertido: {texto[::-1]}")

print()

# ==========================================================
# Curiosidade
# ==========================================================

# O índice final do fatiamento nunca é incluído.
#
# Exemplo:
#
# texto[0:3]
#
# Retorna as posições:
#
# 0
# 1
# 2
#
# A posição 3 não faz parte do resultado.

print(texto[0:3])

print()

# ==========================================================
# Importante
# ==========================================================

# Strings são imutáveis.
#
# O fatiamento NÃO altera a string original.
# Ele apenas retorna uma nova string contendo
# os caracteres selecionados.

print(palavra)
print(palavra[::-1])
