
"""
Python - Dados Mutáveis e Imutáveis

Em Python, os objetos podem ser classificados, entre outras
características, como mutáveis ou imutáveis.

- Imutáveis: não podem ser modificados após sua criação.
- Mutáveis: podem ter seu conteúdo alterado após sua criação.

Exemplos de tipos imutáveis:
- int   : números inteiros.
- float : números decimais.
- str   : strings (textos).
- bool  : valores True e False.
- tuple : tuplas.

Exemplos de tipos mutáveis:
- list : listas.
- dict : dicionários.
- set  : conjuntos.

Conceitos importantes:
- Atribuição: associa uma variável a um objeto.
- Referência: permite que variáveis apontem para o mesmo objeto.
- copy(): cria uma cópia superficial de uma lista.

Observação:
Quando duas variáveis apontam para a mesma lista, uma alteração
feita por meio de qualquer uma delas pode ser observada pela outra.
"""

# ==========================================================
# Exemplo 1 - Atribuindo novos valores a uma string
# ==========================================================

# Strings são imutáveis: seu conteúdo não pode ser alterado
# diretamente após a criação do objeto.
nome = "João"

# A variável nome passa a referenciar a string "Arthur".
# A string original "João" não é modificada.
nome = "Arthur"

print(nome)

print()

# ==========================================================
# Exemplo 2 - Modificando uma lista
# ==========================================================

# Listas são mutáveis, ou seja, podemos modificar seu conteúdo.
lista = [10, 20]

# append() adiciona um elemento à própria lista.
lista.append(30)

print(lista)

print()

# ==========================================================
# Exemplo 3 - Duas variáveis apontando para a mesma lista
# ==========================================================

lista1 = [10, 20, 30]

# Atribuir lista1 a lista2 não cria uma nova lista.
# As duas variáveis passam a referenciar o mesmo objeto.
lista2 = lista1

# A alteração feita por lista2 também pode ser vista por lista1.
lista2.append(40)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

print()

# ==========================================================
# Exemplo 4 - Criando uma cópia independente com copy()
# ==========================================================

lista3 = [10, 20, 30]

# copy() cria uma nova lista com os mesmos elementos.
lista4 = lista3.copy()

# A alteração é feita somente na nova lista.
lista4.append(40)

print(f"Lista original: {lista3}")
print(f"Lista copiada: {lista4}")
