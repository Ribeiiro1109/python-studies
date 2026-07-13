"""
Python - Formatação de Strings com f-strings

As f-strings permitem formatar textos e valores de maneira simples
e legível.

Além de inserir variáveis, também é possível definir o alinhamento,
a quantidade de casas decimais, sinais, preenchimento com caracteres,
representação hexadecimal e flags de conversão.

Principais especificadores:

s  -> String
d  -> Número inteiro
f  -> Número de ponto flutuante
x  -> Hexadecimal (letras minúsculas)
X  -> Hexadecimal (letras maiúsculas)

Casas decimais:

:.2f  -> Exibe duas casas decimais

Alinhamento:

>  -> Alinha à direita
<  -> Alinha à esquerda
^  -> Centraliza

Preenchimento:

0>10 -> Preenche com zeros até completar 10 caracteres

Flags de conversão:

!s -> str()
!r -> repr()
!a -> ascii()
"""

# ==========================================================
# Exemplo 1 - Exibindo uma string
# ==========================================================

variavel = "ABC"

print(f"{variavel}")

print()

# ==========================================================
# Exemplo 2 - Alinhamento de texto
# ==========================================================

# O número indica a largura mínima do campo.

print(f"|{variavel:>10}|")   # Alinhado à direita
print(f"|{variavel:<10}|")   # Alinhado à esquerda
print(f"|{variavel:^10}|")   # Centralizado

print()

# ==========================================================
# Exemplo 3 - Formatação de números
# ==========================================================

numero = 1000.4873648123746

# Explicação:
#
# 0  -> Preenche espaços vazios com zeros
# =  -> Mantém o sinal antes dos zeros
# +  -> Sempre exibe o sinal (+ ou -)
# 10 -> Largura mínima de 10 caracteres
# ,  -> Separador de milhares
# .1f -> Exibe uma casa decimal

print(f"{numero:0=+10,.1f}")

print()

# ==========================================================
# Exemplo 4 - Representação hexadecimal
# ==========================================================

numero = 1500

print(f"O hexadecimal de {numero} é {numero:08X}")

print()

# ==========================================================
# Exemplo 5 - Flags de conversão
# ==========================================================

# !r utiliza repr(), exibindo a representação "oficial"
# do objeto.

print(f"{variavel!r}")

print()

# ==========================================================
# Curiosidade
# ==========================================================

# repr() é muito utilizado durante o desenvolvimento
# para facilitar a depuração (debug) de programas.

print(repr(variavel))

print()

# ==========================================================
# Importante
# ==========================================================

# As f-strings são atualmente a forma mais recomendada
# para formatar strings em Python, pois tornam o código
# mais legível e fácil de manter.