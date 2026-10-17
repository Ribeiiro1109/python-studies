
"""
Python - Iteráveis e Iteradores (iter, next e StopIteration)

Um iterável é um objeto que permite percorrer seus elementos,
como strings e objetos produzidos por range().

Um iterador é um objeto que fornece um elemento por vez,
mantendo o controle da posição atual durante a iteração.

- iter(): obtém um iterador a partir de um objeto iterável.
- next(): retorna o próximo elemento fornecido pelo iterador.
- StopIteration: exceção que indica que não há mais elementos
  disponíveis no iterador.

Observação:
Quando todos os elementos são consumidos, uma nova chamada a
next() gera a exceção StopIteration.
"""

# ==========================================================
# Exemplo 1 - Criando um iterador com iter()
# ==========================================================

# A string é um objeto iterável, pois permite percorrer suas letras.
texto = "Python"

# A função iter() obtém um iterador para a string.
iterador = iter(texto)

# A função next() retorna um elemento por vez.
print(next(iterador))  # P
print(next(iterador))  # y
print(next(iterador))  # t
print(next(iterador))  # h
print(next(iterador))  # o
print(next(iterador))  # n

# Atenção:
# Uma nova chamada a next(iterador) geraria StopIteration,
# pois todas as letras já foram consumidas.

print()

# ==========================================================
# Exemplo 2 - Percorrendo um iterador com while e try/except
# ==========================================================

# A string "Ribeiro" é um objeto iterável.
texto2 = "Ribeiro"

# Obtém um iterador para percorrer os caracteres da string.
iterador2 = iter(texto2)

# O laço continua até que não existam mais elementos.
while True:
    try:
        # Obtém o próximo caractere do iterador.
        letra = next(iterador2)

        # Exibe o caractere obtido.
        print(letra)

    except StopIteration:
        # Encerra o laço quando todos os caracteres forem percorridos.
        break
