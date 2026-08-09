"""
Python - Conversão de Tipos (Type Casting)

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

# ==========================================================
# Exemplo 1 - Conversão para inteiro (int)
# ==========================================================

# Não é possível somar diretamente uma string com um número inteiro.
# Essa operação gera um erro do tipo TypeError.

# print("1" + 1)

# A função int() converte uma string contendo um número inteiro
# para o tipo int.
print(int("1") + 1)

print()

# ==========================================================
# Exemplo 2 - Conversão para ponto flutuante (float)
# ==========================================================

# A função float() converte uma string contendo um número decimal
# para o tipo float.
print(float("-1.0") + 3)

print()

# ==========================================================
# Exemplo 3 - Conversão para booleano (bool)
# ==========================================================

# A função bool() converte um valor para o tipo booleano.

# Uma string vazia resulta em False.
print(bool(""))  # False

# Qualquer string contendo pelo menos um caractere
# (inclusive um espaço) resulta em True.
print(bool(" "))  # True

print()

# ==========================================================
# Exemplo 4 - Conversão para string (str)
# ==========================================================

# Strings podem ser concatenadas utilizando o operador +.
print("a" + "b")

# A função str() converte um valor para o tipo string,
# permitindo a concatenação com outras strings.
print(str(2) + "b")

print()

# ==========================================================
# Curiosidade
# ==========================================================

# Alguns valores são considerados False pelo Python:
#
# bool(0)        -> False
# bool(0.0)      -> False
# bool("")       -> False
#
# Qualquer outro número diferente de zero e qualquer
# string não vazia são considerados True.

print(bool(0))
print(bool(1))
print(bool(-10))
print(bool("Python"))

print()

# ==========================================================
# Atenção
# ==========================================================

# A conversão só funciona quando o valor possui um formato válido.
# Caso contrário, será gerada uma exceção do tipo ValueError.

# Exemplos:
#
# print(int("abc"))     # ValueError
# print(float("texto")) # ValueError
#
# Esses exemplos permanecem comentados para que o programa
# execute normalmente.

# ==========================================================
# Boa prática
# ==========================================================

# Sempre que receber dados do usuário utilizando a função input(),
# lembre-se de que o valor retornado será uma string.
#
# Na maioria das vezes será necessário converter esse valor
# utilizando int() ou float().