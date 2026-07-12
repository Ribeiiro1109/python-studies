"""
Python - Operador Lógico NOT

O operador lógico `not` é utilizado para inverter o valor lógico
de uma expressão.

Funcionamento:

not True   -> False
not False  -> True

Esse operador é muito utilizado em estruturas condicionais para
verificar se uma condição NÃO foi satisfeita.
"""

# ==========================================================
# Exemplo 1 - Invertendo valores booleanos
# ==========================================================

# O operador "not" transforma True em False.
print(not True)   # False

# O operador "not" transforma False em True.
print(not False)  # True

print()

# ==========================================================
# Exemplo 2 - Utilizando o operador NOT em comparações
# ==========================================================

# O resultado da comparação é invertido.

print(not 10 == 10)  # False
print(not 10 == 5)   # True

print()

# ==========================================================
# Exemplo 3 - Utilizando NOT com variáveis
# ==========================================================

usuario_logado = False

# Como o usuário não está logado (False),
# o operador "not" inverte o resultado para True.
if not usuario_logado:
    print("Faça login para continuar.")

print()

# ==========================================================
# Importante
# ==========================================================

# O operador "not" sempre inverte o valor lógico da expressão
# que vem logo após ele.
# Exemplos:
#
# True  -> False
# False -> True
#
# O operador também pode ser utilizado em comparações,
# chamadas de funções e expressões booleanas.
