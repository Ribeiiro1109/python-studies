"""
Python - A Função print()

A função print() é utilizada para exibir informações no terminal.

É uma das funções mais utilizadas em Python e serve para mostrar
textos, números, variáveis e resultados de expressões.

Alguns parâmetros úteis da função print():

sep  -> Define o separador entre os valores exibidos.
end  -> Define o caractere exibido ao final da impressão
        (o padrão é uma quebra de linha "\n").
"""

# ==========================================================
# Exemplo 1 - Exibindo vários valores
# ==========================================================

# Quando vários valores são informados, o Python utiliza
# um espaço como separador padrão.
print(12, 13)

print()

# ==========================================================
# Exemplo 2 - Alterando o separador com "sep"
# ==========================================================

# O parâmetro "sep" (separator) permite definir o caractere
# que separará os valores exibidos.
print(9, 10, 11, sep="-")

print()

# ==========================================================
# Exemplo 3 - Alterando o final da impressão com "end"
# ==========================================================

# Por padrão, o print() termina com uma quebra de linha (\n).
# O parâmetro "end" permite alterar esse comportamento.

print("Python", end=" -> ")
print("Curso")

print()

# ==========================================================
# Curiosidade
# ==========================================================

# É possível utilizar "sep" e "end" ao mesmo tempo.

print("A", "B", "C", sep=" | ", end=".\n")

print()

# ==========================================================
# Importante
# ==========================================================

# A função print() é muito utilizada para:
#
# - Exibir informações ao usuário;
# - Testar partes do código durante o desenvolvimento;
# - Facilitar a identificação de erros (debug).
#
# Conforme você avançar nos estudos, descobrirá outras formas
# de inspecionar o código, mas o print() continuará sendo uma
# ferramenta muito útil.