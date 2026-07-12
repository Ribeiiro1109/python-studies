"""
Python - Operador Lógico OR

O operador lógico `or` é utilizado para combinar duas ou mais condições.

Uma expressão utilizando `or` será considerada verdadeira (True)
quando pelo menos uma das condições for verdadeira.

Somente quando todas as condições forem falsas,
o resultado será False.

Sintaxe:

condicao1 or condicao2

Exemplos:

True or True     -> True
True or False    -> True
False or True    -> True
False or False   -> False

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

# Converte a senha para inteiro.
senha = int(senha)

senha_permitida = 123456

# O operador "or" exige que pelo menos uma condição
# seja verdadeira.
#
# Neste exemplo, o usuário pode digitar:
# E ou e
#
# Em ambos os casos o acesso será permitido,
# desde que a senha esteja correta.
if (entrada == "E" or entrada == "e") and senha == senha_permitida:
    print("Você entrou no sistema.")

elif (entrada == "E" or entrada == "e") and senha != senha_permitida:
    print("Senha incorreta.")

elif entrada == "S" or entrada == "s":
    print("Você saiu do sistema.")

else:
    print("Opção inválida.")

print()

# ==========================================================
# Exemplo 2 - Utilizando o operador OR
# ==========================================================

# Basta uma condição ser verdadeira para que
# o resultado final seja True.

print(True or True)        # True
print(True or False)       # True
print(False or True)       # True
print(False or False)      # False

print()

# O mesmo comportamento ocorre com mais de duas condições.

print(True or True or False)      # True
print(False or False or True)     # True
print(False or False or False)    # False

print()

# ==========================================================
# Exemplo 3 - Valores truthy e falsy
# ==========================================================

# O operador "or" retorna o primeiro valor considerado
# verdadeiro (truthy).

print(0 or False or "Python")
print("" or None or 100)

print()

# ==========================================================
# Importante
# ==========================================================

# O Python avalia as condições da esquerda para a direita.
#
# Assim que encontra uma condição verdadeira em uma expressão
# utilizando "or", ele pode interromper a avaliação das
# demais condições.
#
# Esse comportamento é conhecido como
# "short-circuit evaluation" (avaliação de curto-circuito).