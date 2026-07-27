"""
Python - Strings

Uma string (str) é o tipo de dado utilizado para representar textos
em Python.

Python é uma linguagem de programação com tipagem dinâmica e forte,
ou seja, o tipo de uma variável é definido automaticamente em tempo
de execução e as operações entre tipos incompatíveis geram erros.

As strings podem ser delimitadas por:

- Aspas simples ('')
- Aspas duplas ("")

Também é possível utilizar caracteres de escape e strings literais
(raw strings) para situações específicas.
"""

# ==========================================================
# Exemplo 1 - Strings com aspas simples e aspas duplas
# ==========================================================

print('João Victor')
print("João Victor")

print()

# ==========================================================
# Exemplo 2 - Utilizando caracteres de escape
# ==========================================================

# O caractere "\" permite inserir aspas do mesmo tipo
# utilizadas para delimitar a string.

print("João \"Victor\"")

print()

# ==========================================================
# Exemplo 3 - Raw Strings (r)
# ==========================================================

# O prefixo "r" faz com que a barra invertida (\)
# seja interpretada literalmente.

print(r"João \"Victor\"")

print()

# ==========================================================
# Exemplo 4 - Misturando tipos de aspas
# ==========================================================

# Não é necessário utilizar o caractere de escape
# quando as aspas internas são diferentes das externas.

print("João 'Victor'")
print('João "Victor"')

print()

# ==========================================================
# Exemplo 5 - Strings podem conter diversos caracteres
# ==========================================================

print("Python")
print("12345")
print("Olá, mundo!")
print("Curso de Python")

print()

# ==========================================================
# Curiosidade
# ==========================================================

# Uma string pode estar vazia.

print("")
print('')

print()

# ==========================================================
# Importante
# ==========================================================

# Apesar de representarem números visualmente,
# os valores abaixo continuam sendo strings.

print("10")
print("3.14")

# Para realizar operações matemáticas, será necessário
# converter esses valores para int ou float,
# assunto que será estudado mais adiante.