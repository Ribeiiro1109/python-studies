"""
Python - Interpolação de Strings com o Operador %

Antes das f-strings e do método format(), a forma mais comum de
formatar strings em Python era utilizando o operador %.

Esse recurso ainda existe e pode ser encontrado em códigos legados
(projetos mais antigos).

Principais especificadores:

%s -> String (str)
%d ou %i -> Número inteiro (int)
%f -> Número de ponto flutuante (float)
%x -> Hexadecimal com letras minúsculas
%X -> Hexadecimal com letras maiúsculas

Também é possível definir a quantidade de casas decimais para números
de ponto flutuante.

Exemplo:

%.2f -> Exibe duas casas decimais.
"""

# ==========================================================
# Exemplo 1 - Interpolando uma string e um número decimal
# ==========================================================

nome = "Luiz"
preco = 1000.95897643

# %.2f limita a exibição para duas casas decimais.
mensagem = "%s, o preço é R$ %.2f" % (nome, preco)

print(mensagem)

print()

# ==========================================================
# Exemplo 2 - Trabalhando com números hexadecimais
# ==========================================================

numero = 15

# %d exibe o número em decimal.
# %X exibe o número em hexadecimal utilizando letras maiúsculas.
print("O número decimal é %d." % numero)
print("O hexadecimal de %d é %X." % (numero, numero))

print()

# ==========================================================
# Exemplo 3 - Preenchendo com zeros à esquerda
# ==========================================================

# %08X significa:
#
# 0 -> completa com zeros
# 8 -> largura mínima de 8 caracteres
# X -> hexadecimal em letras maiúsculas

print("Hexadecimal com zeros: %08X" % numero)

print()

# ==========================================================
# Exemplo 4 - Outros exemplos de interpolação
# ==========================================================

idade = 20
altura = 1.78

print("Nome: %s" % nome)
print("Idade: %d anos" % idade)
print("Altura: %.2f m" % altura)

print()

# ==========================================================
# Importante
# ==========================================================

# A interpolação utilizando o operador % ainda funciona,
# porém atualmente é mais comum utilizar:
#
# • f-strings
# • método format()
#
# Mesmo assim, é importante conhecer esse recurso,
# pois ele ainda aparece em projetos antigos e em alguns
# códigos legados.

print()

# ==========================================================
# Curiosidade
# ==========================================================

# O valor armazenado na variável "preco" possui várias casas
# decimais, mas "%.2f" altera apenas a forma como ele é exibido.
#
# O valor original continua o mesmo.

print(preco)
print("%.2f" % preco)