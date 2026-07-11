"""
Python - Operador Lógico AND

O operador lógico `and` é utilizado para combinar duas ou mais condições.

Uma expressão utilizando `and` será considerada verdadeira (True)
somente quando todas as condições forem verdadeiras.

Se pelo menos uma condição for falsa (False), toda a expressão
será considerada falsa.

Sintaxe:

condicao1 and condicao2

Exemplos:

True and True    -> True
True and False   -> False
False and True   -> False
False and False  -> False

Em Python, alguns valores são considerados falsos (falsy):

- 0
- 0.0
- ""
- False
- None

Qualquer outro valor é considerado verdadeiro (truthy).
"""

# ==========================================================
# Exemplo 1 - Simulando um login
# ==========================================================

entrada = input("[E]ntrar ou [S]air: ")
senha = input("Digite a senha: ")

# Converte a senha informada para inteiro.
senha = int(senha)

senha_permitida = 123456

# O operador "and" exige que todas as condições sejam verdadeiras.
#
# Neste exemplo:
# - O usuário precisa escolher a opção "E";
# - A senha informada deve ser igual à senha permitida.
#
# Somente quando as duas condições forem verdadeiras
# o acesso será liberado.
if entrada == "E" and senha == senha_permitida:
    print("Você entrou no sistema.")

elif entrada == "E" and senha != senha_permitida:
    print("Senha incorreta.")

elif entrada == "S":
    print("Você saiu do sistema.")

else:
    print("Opção inválida.")

print()

# ==========================================================
# Exemplo 2 - Utilizando o operador AND
# ==========================================================

# Todas as condições precisam ser verdadeiras para que
# o resultado final seja True.

print(True and True)       # True
print(True and False)      # False
print(False and True)      # False
print(False and False)     # False

print()

# O mesmo comportamento ocorre quando há mais de duas condições.
print(True and True and True)        # True
print(True and False and True)       # False
print(True and True and False)       # False

print()

# ==========================================================
# Exemplo 3 - Valores falsy
# ==========================================================

# A função bool() mostra como o Python interpreta um valor
# em um contexto booleano.

print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(False))
print(bool(None))

print()

# ==========================================================
# Importante
# ==========================================================

# O Python avalia as condições da esquerda para a direita.
# Assim que encontra um valor falso em uma expressão com "and",
# ele pode interromper a avaliação das demais condições.
#
# Esse comportamento é conhecido como "short-circuit evaluation"
# (avaliação de curto-circuito).

print(False and True)
print(False and False)
print(True and False)