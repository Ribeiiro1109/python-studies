
"""
Python - Listas (list)

Listas são estruturas utilizadas para armazenar vários itens
em uma única variável.

Características das listas:
- São ordenadas: mantêm a ordem dos elementos.
- São mutáveis: permitem adicionar, alterar e remover elementos.
- Permitem valores duplicados.
- Aceitam elementos de diferentes tipos de dados.
- Utilizam índices que começam em 0.
- Permitem acessar elementos por índices e fatias (slicing).

Formas de criar uma lista:
- []      : forma mais comum de criar uma lista.
- list()  : função que cria uma lista a partir de um iterável.

Principais operações e métodos:
- append(): adiciona um elemento ao final da lista.
- insert(): adiciona um elemento em um índice específico.
- pop()   : remove e retorna um elemento da lista.
- del     : remove um elemento ou uma parte da lista.
- clear() : remove todos os elementos da lista.
- extend(): adiciona os elementos de outro iterável à lista.
- +       : concatena listas, criando uma nova lista.

CRUD em listas:
- Create (criar): criar uma lista ou adicionar elementos.
- Read   (ler): acessar e consultar elementos.
- Update (alterar): modificar elementos existentes.
- Delete (excluir): remover elementos.
"""

# ==========================================================
# Exemplo 1 - Criando e acessando uma lista
# ==========================================================

# Os índices começam em 0, e não em 1.
# Índice:       0         1        2       3
minha_lista = ["maçã", "banana", "uva", "maçã"]

# Acessa o elemento que está no índice 2.
print(minha_lista[2])

# Exibe todos os elementos da lista.
print(minha_lista)

print()

# ==========================================================
# Exemplo 2 - Descobrindo o tamanho de uma lista
# ==========================================================

# A função len() retorna a quantidade de elementos da lista.
print(f"A quantidade de itens na lista é: {len(minha_lista)}")

print()

# ==========================================================
# Exemplo 3 - Listas com diferentes tipos de dados
# ==========================================================

lista1 = ["maçã", "banana", "uva"]
lista2 = [1, 2, 3, 4, 5]
lista3 = [True, False, False]

# Uma lista pode armazenar diferentes tipos de dados.
lista4 = ["maçã", 5, True, 20, "uva"]

# Exibe o tipo de dado da variável lista4.
print(type(lista4))

print()

# ==========================================================
# Exemplo 4 - Removendo e adicionando elementos
# ==========================================================

minha_lista2 = [0, 10, 20, 30, 40, 50]

print(f"Lista original: {minha_lista2}")

# del remove o elemento localizado no índice 5.
del minha_lista2[5]

# append() adiciona o valor 60 ao final da lista.
minha_lista2.append(60)

# pop() remove e retorna o último elemento da lista.
valor_removido1 = minha_lista2.pop()

# Adiciona o valor 70 ao final da lista.
minha_lista2.append(70)

# Remove e retorna o último elemento novamente.
valor_removido2 = minha_lista2.pop()

print(f"Lista atualizada: {minha_lista2}")
print(f"Primeiro valor removido com pop(): {valor_removido1}")
print(f"Segundo valor removido com pop(): {valor_removido2}")

print()

# ==========================================================
# Exemplo 5 - Adicionando elementos com insert()
# ==========================================================

minha_lista3 = [2, 4, 6, 8]

# insert(índice, valor) insere o elemento na posição escolhida.
minha_lista3.insert(0, 0)

# Adiciona o valor 10 ao final da lista.
minha_lista3.append(10)

print(minha_lista3)

print()

# ==========================================================
# Exemplo 6 - Concatenando listas com o operador +
# ==========================================================

lista_a = ["A", "B", "C"]
lista_b = ["D", "E", "F"]

# O operador + cria uma nova lista com os elementos das duas listas.
lista_c = lista_a + lista_b

print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C (concatenação): {lista_c}")

print()

# ==========================================================
# Exemplo 7 - Estendendo uma lista com extend()
# ==========================================================

lista_a = ["A", "B", "C"]
lista_b = ["D", "E", "F"]

# extend() adiciona os elementos de lista_b ao final de lista_a.
lista_a.extend(lista_b)

print(f"Lista A após extend(): {lista_a}")

print()

# ==========================================================
# Exemplo 8 - Removendo todos os elementos com clear()
# ==========================================================

lista_numeros = [10, 20, 30, 40]

print(f"Lista antes de clear(): {lista_numeros}")

# clear() remove todos os elementos, mas mantém a lista existente.
lista_numeros.clear()

print(f"Lista depois de clear(): {lista_numeros}")
