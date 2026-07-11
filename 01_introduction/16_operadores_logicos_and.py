"""
Python - Operadores Lógicos

Os operadores lógicos são utilizados para combinar expressões booleanas
(True ou False).

Operadores disponíveis:

and  -> Retorna True apenas se todas as condições forem verdadeiras.
or   -> Retorna True se pelo menos uma condição for verdadeira.
not  -> Inverte o valor lógico de uma expressão.

Valores considerados False (falsy):

- 0
- 0.0
- ""
- False
- None

Qualquer outro valor é considerado True (truthy).
"""

# ==========================================================
# Exemplo 1 - Simulando um login
# ==========================================================

entrada = input("[E]ntrar ou [S]air: ")
senha = input("Digite a senha: ")

# Converte a senha informada para inteiro.
senha = int(senha)

senha_permitida = 123456

# O Python avalia as condições da esquerda para a direita.
# Se uma condição do operador "and" for False,
# as demais podem nem ser avaliadas.
# O operador "and" exige que todas as condições sejam verdadeiras.
if entrada == "E" and senha == senha_permitida:
    print("Você entrou.")

elif entrada == "E" and senha != senha_permitida:
    print("Senha incorreta.")

elif entrada == "S":
    print("Você saiu.")

else:
    print("Opção inválida.")

print()

# ==========================================================
# Exemplo 2 - Operador AND
# ==========================================================

# O resultado será True apenas quando todas as expressões
# forem verdadeiras.
print(True and False and True)
print(True and True and False)
print(False and True and True)

print()

# ==========================================================
# Exemplo 3 - Valores falsy
# ==========================================================

# A função bool() mostra como o Python interpreta um valor
# em um contexto booleano.
print(bool(0))
print(bool(""))
print(bool(0.0))
print(bool(None))