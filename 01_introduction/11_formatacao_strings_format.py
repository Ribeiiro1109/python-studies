"""
Python - Formatação de Strings com o método format()

O método format() permite inserir valores em uma string utilizando
campos de substituição, definidos entre chaves ({}).

Também é possível aplicar formatações específicas, como definir
a quantidade de casas decimais de um número.
"""

# Valores que serão inseridos na string.
a = "A"
b = "B"
c = 1.50

# Campos entre chaves ({}) serão substituídos pelos valores
# informados no método format().
#
# {:.2f} significa:
# - f -> número de ponto flutuante (float)
# - .2 -> exibir duas casas decimais
string = "a={nome1} b={nome2} c={nome3:.2f}"

# Associa cada valor ao respectivo campo da string.
formato = string.format(
    nome1=a,
    nome2=b,
    nome3=c,
)

print(formato)