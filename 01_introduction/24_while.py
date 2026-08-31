"""
Python - Estruturas de Repetição (while)

A estrutura de repetição while (enquanto) permite executar um bloco
de código repetidamente enquanto uma determinada condição for verdadeira.

A cada repetição, a condição é verificada novamente.

- while    : repete um bloco de código enquanto a condição for verdadeira.
- break    : interrompe imediatamente o loop.
- continue : interrompe a repetição atual e passa para a próxima.
- loop infinito: acontece quando a condição do while nunca se torna falsa.

Operadores de atribuição:

- =   : atribuição
- +=  : soma e atribui
- -=  : subtrai e atribui
- *=  : multiplica e atribui
- /=  : divide e atribui
- //= : divisão inteira e atribui
- **= : potência e atribui
- %=  : módulo (resto da divisão) e atribui
"""

# ==========================================================
# Exemplo 1 - Repetindo uma ação com while
# ==========================================================

# Variável utilizada para controlar a quantidade de repetições.
contador = 0

# O bloco será executado enquanto contador for menor ou igual a 10.
while contador <= 10:
    print(contador)

    # Aumenta o contador em 1 a cada repetição.
    # É importante alterar a variável para que a condição
    # eventualmente se torne falsa e o loop termine.
    contador += 1

print("Acabou!")

print()

# ==========================================================
# Exemplo 2 - Interrompendo um loop com break
# ==========================================================

i = 1

while i < 11:
    print(i)

    # Interrompe o loop quando i for igual a 6.
    if i == 6:
        break

    i += 1

print("Loop interrompido.")

print()

# ==========================================================
# Exemplo 3 - Pulando uma repetição com continue
# ==========================================================

numero = 0

while numero <= 50:
    # Aumenta o número antes de verificar se ele é par.
    numero += 1

    # Verifica se o número é ímpar.
    # Se for, o continue pula o restante dessa repetição
    # e volta para o início do while.
    if numero % 2 != 0:
        continue

    # Apenas os números pares chegam até este print.
    print(numero)

    # Encerra o loop quando chegar ao número 50.
    if numero == 50:
        break

print("Loop finalizado.")

print()

# ==========================================================
# Observação - Cuidado com loops infinitos
# ==========================================================

# Se a variável utilizada na condição não for alterada,
# o loop pode nunca terminar.

# Exemplo de loop infinito:
#
# contador = 0
#
# while contador <= 10:
#     print(contador)
#
# Nesse caso, contador nunca muda de valor,
# portanto a condição continuará sendo verdadeira.