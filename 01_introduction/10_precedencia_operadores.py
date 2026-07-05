"""
Python - Precedência dos Operadores

Quando uma expressão possui vários operadores, o Python segue uma
ordem de prioridade para determinar quais operações serão executadas
primeiro.

Ordem de precedência:

1. Parênteses ()
2. Exponenciação (**)
3. Multiplicação (*), divisão (/), divisão inteira (//) e módulo (%)
4. Adição (+) e subtração (-)
"""

# Primeiro é realizada a exponenciação (1 ** 5),
# depois as operações de adição.
conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

# Primeiro são resolvidos os parênteses.
# Em seguida, ocorre a conversão para inteiro com int().
# Depois é realizada a exponenciação e, por fim, a multiplicação.
conta_2 = 2 * (1 + int(0.5 + 2)) ** (5 + 5)
print(conta_2)