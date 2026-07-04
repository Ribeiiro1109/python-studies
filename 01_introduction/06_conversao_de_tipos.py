"""
Python - Conversão de tipos (Type Casting)

A conversão de tipos é o processo de transformar um valor de um tipo
em outro.

Esse processo também é conhecido como:
- Type conversion
- Type casting
- Coercion

Os principais tipos primitivos e imutáveis estudados até o momento são:
- str
- int
- float
- bool
"""

# Não é possível somar diretamente uma string com um número inteiro.
# Essa operação gera um erro do tipo TypeError.

# print("1" + 1)

# A função int() converte uma string contendo um número inteiro
# para o tipo int.
print(int("1") + 1)

# A função float() converte uma string contendo um número decimal
# para o tipo float.
print(float("-1.0") + 3)

# A função bool() converte um valor para o tipo booleano.
# Uma string vazia resulta em False.
print(bool(""))  # False

# Uma string contendo qualquer caractere (inclusive um espaço)
# resulta em True.
print(bool(" "))  # True

# Strings podem ser concatenadas utilizando o operador +.
print("a" + "b")

# A função str() converte um valor para o tipo string,
# permitindo a concatenação com outras strings.
print(str(2) + "b")