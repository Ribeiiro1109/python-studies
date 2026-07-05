"""
Python - f-strings

As f-strings (formatted string literals) são uma forma simples e moderna
de formatar strings.

Esse recurso está disponível a partir do Python 3.6.

Para utilizar uma f-string, basta adicionar a letra "f" antes das aspas.
Tudo o que estiver entre chaves ({}) será interpretado como uma
expressão Python.
"""

# ==========================================================
# Exemplo básico
# ==========================================================

nome = "João"
idade = 20

print(f"Meu nome é {nome} e tenho {idade} anos.")

print()

# ==========================================================
# Inserindo múltiplas variáveis
# ==========================================================

nome = "Maria"
idade = 25
cidade = "Belo Horizonte"

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Cidade: {cidade}")

print()

# ==========================================================
# Realizando operações dentro das chaves
# ==========================================================

numero = 10

print(f"Número: {numero}")
print(f"Dobro: {numero * 2}")
print(f"Triplo: {numero * 3}")
print(f"Quadrado: {numero ** 2}")

print()

# ==========================================================
# Utilizando operadores aritméticos
# ==========================================================

a = 10
b = 3

print(f"Soma: {a + b}")
print(f"Subtração: {a - b}")
print(f"Multiplicação: {a * b}")
print(f"Divisão: {a / b}")
print(f"Divisão inteira: {a // b}")
print(f"Resto da divisão: {a % b}")

print()

# ==========================================================
# Formatando números decimais
# ==========================================================

pi = 3.14159265359

# O especificador :.nf define quantas casas decimais serão exibidas.
print(f"Valor original: {pi}")
print(f"Uma casa decimal: {pi:.1f}")
print(f"Duas casas decimais: {pi:.2f}")
print(f"Três casas decimais: {pi:.3f}")

print()

# ==========================================================
# Exemplo completo
# ==========================================================

nome = "João"
idade = 20
altura = 1.7564

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura:.2f} m")

# Expressões também podem ser avaliadas diretamente nas chaves.
print(f"Ano de nascimento aproximado: {2026 - idade}")